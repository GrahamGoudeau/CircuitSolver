# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Two_Prong_Component_Types = enum('RESISTOR', 'CAPACITOR')

class Node(object):
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

class Component(Node):
    def __init__(self, id):
        super(Component, self).__init__(id)

class Component_Two_Prongs(Component):
    def __init__(self, id, junctionA, junctionB):
        super(Component_Two_Prongs, self).__init__(id)
        self.junctionA = junctionA
        self.junctionB = junctionB

class Junction(Node):
    def __init__(self, id):
        super(Junction, self).__init__(id)
        self.connections = [] # array of nodes

    def add_connection(self, node):
        self.connections.append(node)

class Resistor(Component_Two_Prongs):
    def __init__(self, id, resistance, junctionA, junctionB):
        super(Resistor, self).__init__(id, junctionA, junctionB)
        self.resistance = resistance

class Capacitor(Component_Two_Prongs):
    def __init__(self, id, capacitance, junctionA, junctionB):
        super(Capacitor, self).__init__(id, junctionA, junctionB)
        self.capacitance = capacitance

class Circuit(object):
    def __init__(self, junctions=[]):
        self.junctions = junctions
        self.current_id = 1 # increment every time we assign it
        self.node_map = {}

    def debug_map(self):
        keys = self.node_map.keys()
        for key in keys:
            print "Node id: " + key + " is " + str(self.node_map[key])
            if not isinstance(self.node_map[key], Junction):
                print "\tConnections: " + str(self.node_map[key].junctionA) + " " + str(self.node_map[key].junctionB)
            if isinstance(self.node_map[key], Resistor):
                print "\tResistance: " + str(self.node_map[key].resistance)
            if isinstance(self.node_map[key], Junction):
                for c in self.node_map[key].connections:
                    print "\tjunction connection id: " + str(c.get_id())

    def __get_unique_id(self):
        ret_value = self.current_id
        self.current_id += 1
        return ret_value

    def add_nodes_to_map(self, nodes):
        for node in nodes:
            self.node_map[str(node.get_id())] = node

    def add_node_to_map(self, node):
        self.node_map[str(node.get_id())] = node

    # expects two junction ids or None
    def add_two_prong_component(self, component_type,
                        value, junctionA=None, junctionB=None):
        id = self.__get_unique_id()
        if junctionA is None:
            junctionA = self.__get_unique_id()
        if junctionB is None:
            junctionB = self.__get_unique_id()

        if component_type == Two_Prong_Component_Types.RESISTOR:
            class_type = Resistor
        elif component_type == Two_Prong_Component_Types.CAPACITOR:
            class_type = Capacitor
        else:
            raise Exception("Invalid component type")

        component = class_type(id, value, junctionA, junctionB)
        j1 = self.node_map.get(str(junctionA), None)
        if j1 is None:
            j1 = Junction(junctionA)
        j1.add_connection(component)

        j2 = self.node_map.get(str(junctionB), None)
        if j2 is None:
            j2 = Junction(junctionB)
        j2.add_connection(component)

        self.add_nodes_to_map([component, j1, j2])
        return (junctionA, junctionB)

    # expects the ids of both junctions
    def connect_junctions(self, junctionA, junctionB):
        j1 = self.node_map[str(junctionA)]
        j2 = self.node_map[str(junctionB)]
        j1.connections.append(j2)
        j2.connections.append(j1)

    # takes a list of ids of other nodes
    def __add_junction(self, connections=[]): # camel case or underscore
        junction = Junction(self.__get_unique_id(), connections)
        self.node_map[str(junction.get_id())] = junction
        self.junctions.append(junction)

    def get_all_junctions(self):
        keys = self.node_map.keys()
        return [self.node_map[x] for x in keys if isinstance(self.node_map[x], Junction)]

if __name__ == "__main__":
    circuit = Circuit()
    # returns the ids of the two junctions it creates
    j1, j2 = circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5)
    circuit.add_two_prong_component(Two_Prong_Component_Types.CAPACITOR, 10, j1, j2)
    circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 100, j1, j2)
    circuit.debug_map()

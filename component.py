# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Component_Types = enum('RESISTOR', 'CAPACITOR')

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
    def __init__(self, id, connections):
        super(Junction, self).__init__(id)
        self.connections = connections # array of nodes

class Resistor(Component_Two_Prongs):
    def __init__(self, id, resistance, junctionA, junctionB):
        super(Resistor, self).__init__(id, junctionA, junctionB)
        self.resistance = resistance

class Circuit(object):
    def __init__(self, junctions=[]):
        self.junctions = junctions
        self.current_id = 1 # increment every time we assign it
        self.node_map = {}

    def debug_map(self):
        keys = self.node_map.keys()
        for key in keys:
            print "Node id: " + key + " is " + str(self.node_map[key])
            if isinstance(self.node_map[key], Resistor):
                print "Resistance: " + str(self.node_map[key].resistance)
            if isinstance(self.node_map[key], Junction):
                for c in self.node_map[key].connections:
                    print "junction connection id: " + str(c.get_id())

    def __get_unique_id(self):
        ret_value = self.current_id
        self.current_id += 1
        return ret_value

    def add_node_to_map(self, node):
        self.node_map[str(node.get_id())] = node

    # expects two junction ids or None
    def add_resistor(self, resistance, junctionA=None, junctionB=None):
        id = self.__get_unique_id()
        if junctionA is None:
            junctionA = self.__get_unique_id()
        if junctionB is None:
            junctionB = self.__get_unique_id()
        resistor = Resistor(id, resistance, junctionA, junctionB)
        j1 = Junction(junctionA, [resistor])
        j2 = Junction(junctionB, [resistor])
        self.add_node_to_map(resistor)
        self.add_node_to_map(j1)
        self.add_node_to_map(j2)
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
        return self.junctions

if __name__ == "__main__":
    circuit = Circuit()
    # returns the ids of the two junctions it creates
    j1, j2 = circuit.add_resistor(5)
    circuit.connect_junctions(j1, j2)
    circuit.debug_map()

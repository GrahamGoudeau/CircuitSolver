from Component_Types import Two_Prong_Component_Types, Single_Prong_Component_Types
from Junction import Junction
import Component_Single_Prong
import Component_Two_Prongs

class Circuit(object):
    def __init__(self, junctions=[]):
        self.junctions = junctions
        self.current_id = 1 # increment every time we assign it
        self.node_map = {}

    def debug_map(self):
        keys = self.node_map.keys()
        for key in keys:
            print "Node id: " + key + " is " + str(self.node_map[key])
            if not isinstance(self.node_map[key], Junction) and \
                not isinstance(self.node_map[key], Component_Single_Prong.Open):
                print "\tConnections: " + str(self.node_map[key].junctionA) + " " + str(self.node_map[key].junctionB)
            if isinstance(self.node_map[key], Component_Two_Prongs.Resistor):
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

    # expects a numeric id, returns None if not found
    def get_node(self, id):
        return self.node_map.get(str(id), None)

    # expects two junction ids or None
    def add_two_prong_component(self, component_type,
                        value, junctionA=None, junctionB=None):
        id = self.__get_unique_id()
        if junctionA is None:
            junctionA = self.__get_unique_id()
        if junctionB is None:
            junctionB = self.__get_unique_id()

        if component_type == Two_Prong_Component_Types.RESISTOR:
            class_type = Component_Two_Prongs.Resistor
        elif component_type == Two_Prong_Component_Types.CAPACITOR:
            class_type = Component_Two_Prongs.Capacitor
        else:
            raise Exception('Invalid component type')

        component = class_type(id, value, junctionA, junctionB)
        j1 = self.get_node(junctionA)
        if j1 is None:
            j1 = Junction(junctionA)
        j1.add_connection(component)

        j2 = self.get_node(junctionB)
        if j2 is None:
            j2 = Junction(junctionB)
        j2.add_connection(component)

        self.add_nodes_to_map([component, j1, j2])

        # return a tuple of the junctions that were used
        return (junctionA, junctionB)

    def add_single_prong_component(self, component_type, junction=None):
        id = self.__get_unique_id()
        if junction is None:
            junction = self.__get_unique_id()

        if component_type == Single_Prong_Component_Types.OPEN:
            class_type = Component_Single_Prong.Open
        else:
            raise Exception('Invalid component type')

        component = class_type(id, junction)
        junction_node = self.get_node(junction)
        if junction_node is None:
            junction_node = Junction(junction)
        junction_node.add_connection(component)

        self.add_nodes_to_map([component, junction_node])

        # return the ID of the junction that was used
        return junction

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
    _, y = circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 100, j1)
    circuit.add_single_prong_component(Single_Prong_Component_Types.OPEN, y)
    circuit.debug_map()
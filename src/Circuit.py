from Component_Types import Two_Prong_Component_Types, Single_Prong_Component_Types
from Junction import Junction
import Component_Single_Prong
import Component_Two_Prongs
from Component_Exception import UnknownComponentError, UnrecognizedIdError
import uuid

###############################################################################
class Circuit(object):
    """
    Representation of a circuit. Holds nodes (components and junctions) and 
    information about their connections and properties
    """
    ###########################################################################
    def __init__(self):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        self.node_map = {}

    ###########################################################################
    def debug_map(self):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
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
            if isinstance(self.node_map[key], Component_Single_Prong.Open):
                print "\tConnection: " + str(self.node_map[key].junction)

    ###########################################################################
    def __get_unique_id(self):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        return uuid.uuid4()

    ###########################################################################
    def add_nodes_to_map(self, nodes):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        for node in nodes:
            self.node_map[str(node.get_id())] = node

    ###########################################################################
    def add_node_to_map(self, node):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        self.node_map[str(node.get_id())] = node

    ###########################################################################
    # expects a numeric id, returns None if not found
    def get_node(self, id):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        return self.node_map.get(str(id), None)

    ###########################################################################
    # expects a member of the two prong type enum
    # creates new junctions and assigns IDs if not provided them
    def add_two_prong_component(self, component_type,
                        value, junction_id1=None, junction_id2=None):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        # raise exception if provided an id, but it is unrecognized
        if junction_id1 is not None and str(junction_id1) not in self.node_map:
            raise UnrecognizedIdError(junction_id1)
        if junction_id2 is not None and str(junction_id2) not in self.node_map:
            raise UnrecognizedIdError(junction_id2)

        component_id = self.__get_unique_id()
        if junction_id1 is None:
            junction_id1 = self.__get_unique_id()
        if junction_id2 is None:
            junction_id2 = self.__get_unique_id()

        if component_type == Two_Prong_Component_Types.RESISTOR:
            class_type = Component_Two_Prongs.Resistor
        elif component_type == Two_Prong_Component_Types.CAPACITOR:
            class_type = Component_Two_Prongs.Capacitor
        else:
            raise UnknownComponentError()

        component = class_type(component_id, value, junction_id1, junction_id2)
        junction_node1 = self.get_node(junction_id1)
        if junction_node1 is None:
            junction_node1 = Junction(junction_id1)
        junction_node1.add_connection(component)

        junction_node2 = self.get_node(junction_id2)
        if junction_node2 is None:
            junction_node2 = Junction(junction_id2)
        junction_node2.add_connection(component)

        self.add_nodes_to_map([component, junction_node1, junction_node2])

        # return a tuple of the junctions that were used
        return (junction_id1, junction_id2)

    ###########################################################################
    # expects a member of the single prong type enum
    # creates a new junction and assigns an ID if not provided one
    def add_single_prong_component(self, component_type, junction_id=None):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        # raise exception if provided an id, but it is unrecognized
        if junction_id is not None and str(junction_id) not in self.node_map:
            raise UnrecognizedIdError(junction_id)

        id = self.__get_unique_id()
        if junction_id is None:
            junction_id = self.__get_unique_id()

        if component_type == Single_Prong_Component_Types.OPEN:
            class_type = Component_Single_Prong.Open
        else:
            raise UnknownComponentError()

        component = class_type(id, junction_id)
        junction_node = self.get_node(junction_id)
        if junction_node is None:
            junction_node = Junction(junction_id)
        junction_node.add_connection(component)

        self.add_nodes_to_map([component, junction_node])

        # return the ID of the junction that was used
        return junction_id

    ###########################################################################
    # expects the ids of both junctions, raises KeyException if an invalid ID
    def connect_junctions(self, junctionA, junctionB):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        j1 = self.node_map[str(junctionA)]
        j2 = self.node_map[str(junctionB)]
        j1.add_connection(j2)
        j2.add_connection(j1)

    ###########################################################################
    def get_all_junctions(self):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        keys = self.node_map.keys()
        return [self.node_map[x] for x in keys if isinstance(self.node_map[x], Junction)]

###############################################################################
# run the file as a standalone script to run the test
if __name__ == "__main__":
    circuit = Circuit()
    # returns the ids of the two junctions it creates
    j1, j2 = circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5)
    circuit.add_two_prong_component(Two_Prong_Component_Types.CAPACITOR, 10, j1, j2)
    _, y = circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 100, j1)
    circuit.add_single_prong_component(Single_Prong_Component_Types.OPEN, y)
    circuit.debug_map()


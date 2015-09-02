import os
import sys

dirname = os.path.dirname(__file__)
sys.path.append(os.path.abspath(dirname + '/' + '../..'))

import node.Node as node


###############################################################################
class Junction(node.Node):
    """
    Is an element of a circuit that connects two or more components together.
    Components are never connected directly together
    """
    ###########################################################################
    def __init__(self, id):
        """
        DESCRIPTION
            Constructor for a Junction
        PARAMETERS
            id, int, required
                Unique id of Junction
        RETURNS
            New instance of a Junction
        """
        super(Junction, self).__init__(id)
        self.connections = []  # array of nodes

    ###########################################################################
    def add_connection(self, node):
        """
        DESCRIPTION
            Adds a new connection to the junction, that connection could be
            a component or another junction
        PARAMETERS
            node, Node, required
                Node to connect junction to
        RETURNS
            Nothing
        """
        self.connections.append(node)

###############################################################################

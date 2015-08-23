from Node import Node

###############################################################################
class Junction(Node):
    """
    Is an element of a circuit that connects two or more components together.
    Components are never connected directly together
    """
    ###########################################################################
    def __init__(self, id):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Junction, self).__init__(id)
        self.connections = [] # array of nodes

    ###########################################################################
    def add_connection(self, node):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        self.connections.append(node)

###############################################################################

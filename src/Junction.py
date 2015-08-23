from Node import Node

###############################################################################
class Junction(Node):
    """
    Class Description
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

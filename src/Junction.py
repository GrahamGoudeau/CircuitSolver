from Node import Node

###############################################################################
class Junction(Node):
    """
    Class Description
    """
    ###########################################################################
    def __init__(self, id):
        super(Junction, self).__init__(id)
        self.connections = [] # array of nodes

    ###########################################################################
    def add_connection(self, node):
        self.connections.append(node)

###############################################################################

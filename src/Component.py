from Node import Node

###############################################################################
class Component(Node):
    """
    An element of a circuit that affects the flow of current in some way, or 
    serves some purpose other than connecting other components
    """
    ###########################################################################
    def __init__(self, id):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Component, self).__init__(id)

###############################################################################

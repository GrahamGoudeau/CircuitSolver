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
            Constructor for a component
        PARAMETERS
            id, int, required
                Unique id of component
        RETURNS
            New instance of a component
        """
        super(Component, self).__init__(id)

###############################################################################

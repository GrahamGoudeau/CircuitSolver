from Component import Component

###############################################################################
class Component_Single_Prong(Component):
    """
    Class Description
    """
    ###########################################################################
    def __init__(self, id, junction):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Component_Single_Prong, self).__init__(id)
        self.junction = junction

###############################################################################
class Open(Component_Single_Prong):
    """
    Class Description
    """
    ###########################################################################
    def __init__(self, id, junction):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Open, self).__init__(id, junction)

###############################################################################

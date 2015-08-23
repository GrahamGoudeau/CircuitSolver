from Component import Component

###############################################################################
class Component_Single_Prong(Component):
    """
    A component with only one connection
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
    A circuit component that describes a node to look into the circuit at. 
    When computing equivalent resistance, capacitance, or inductance, 
    there must be two of these in the circuit that define the equivalent 
    resistance, capacitance, or inductance between those points
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

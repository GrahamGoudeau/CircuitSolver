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
            Constructor for a single pronged component
        PARAMETERS
            id, int, required
                Unique id of single pronged component
        RETURNS
            New instance of a single pronged component
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
            Constructor for an open
        PARAMETERS
            id, int, required
                Unique id of the open
            junction, Junction, required
                Junction to connect open to
        RETURNS
            New instance of an open
        """
        super(Open, self).__init__(id, junction)

###############################################################################

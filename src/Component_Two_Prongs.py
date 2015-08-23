from Component import Component

###############################################################################
class Component_Two_Prongs(Component):
    """
    A circuit component that has two connections
    """
    ###########################################################################
    def __init__(self, id, junctionA, junctionB):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Component_Two_Prongs, self).__init__(id)
        self.junctionA = junctionA
        self.junctionB = junctionB

###############################################################################
class Resistor(Component_Two_Prongs):
    """
    Representation of a resistor
    """
    ###########################################################################
    def __init__(self, id, resistance, junctionA, junctionB):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Resistor, self).__init__(id, junctionA, junctionB)
        self.resistance = resistance

###############################################################################
class Capacitor(Component_Two_Prongs):
    """
    Representation of a capacitor
    """
    ###########################################################################
    def __init__(self, id, capacitance, junctionA, junctionB):
        """
        DESCRIPTION
        PARAMETERS
        RETURNS
        """
        super(Capacitor, self).__init__(id, junctionA, junctionB)
        self.capacitance = capacitance

###############################################################################

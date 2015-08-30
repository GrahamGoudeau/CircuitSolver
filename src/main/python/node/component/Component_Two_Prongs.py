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
            Constructor for a two pronged component
        PARAMETERS
            id, int, required
                Unique id of two pronged component
            junctionA, Junction, required
                One of two junctions to connect component to
            junctionB, Junction, required
                Other of two junctions to connect to component to
        RETURNS
            New instance of a two pronged component
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
            Constructor for a resistor
        PARAMETERS
            id, int, required
                Unique id of resistor
            resistance, int, required
                Resistance value of the resistor
            junctionA, Junction, required
                One of two junctions to connect resistor to
            junctionB, Junction, required
                Other junction to connect resistor to
        RETURNS
            New instance of a resistor
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
            Constructor for a resistor
        PARAMETERS
            id, int, required
                Unique id of resistor
            capacitance, int, required
                Capacitance value of the capacitor
            junctionA, Junction, required
                One of two junctions to connect capacitor to
            junctionB, Junction, required
                Other junction to connect capacitor to
        RETURNS
            New instance of a capacitor
        """
        super(Capacitor, self).__init__(id, junctionA, junctionB)
        self.capacitance = capacitance

###############################################################################

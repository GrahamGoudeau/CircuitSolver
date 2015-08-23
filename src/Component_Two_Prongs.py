from Component import Component

###############################################################################
class Component_Two_Prongs(Component):
    ###########################################################################
    def __init__(self, id, junctionA, junctionB):
        super(Component_Two_Prongs, self).__init__(id)
        self.junctionA = junctionA
        self.junctionB = junctionB

###############################################################################
class Resistor(Component_Two_Prongs):
    ###########################################################################
    def __init__(self, id, resistance, junctionA, junctionB):
        super(Resistor, self).__init__(id, junctionA, junctionB)
        self.resistance = resistance

###############################################################################
class Capacitor(Component_Two_Prongs):
    ###########################################################################
    def __init__(self, id, capacitance, junctionA, junctionB):
        super(Capacitor, self).__init__(id, junctionA, junctionB)
        self.capacitance = capacitance

###############################################################################

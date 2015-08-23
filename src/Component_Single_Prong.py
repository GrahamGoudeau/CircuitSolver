from Component import Component

class Component_Single_Prong(Component):
    def __init__(self, id, junction):
        super(Component_Single_Prong, self).__init__(id)
        self.junction = junction

class Open(Component_Single_Prong):
    def __init__(self, id, junction):
        super(Open, self).__init__(id, junction)

# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Two_Prong_Component_Types = enum('RESISTOR', 'CAPACITOR')

Single_Prong_Component_Types = enum('OPEN')


from Error import Error


class NonUniqueComponentNameError(Error):
    def __init__(self, name):
        super(NonUniqueComponentNameError, self)\
            .__init__('Non unique component name: \'' + name + '\'')


class UnknownJSONTypeError(Error):
    def __init__(self, type):
        super(UnknownJSONTypeError, self)\
            .__init__('Unknown JSON type: \'' + type + '\'')


class WrongNumberOfJunctions(Error):
    def __init__(self, type):
        super(WrongNumberOfJunctions, self)\
            .__init__('Incorrect number of junctions for \'' + type + '\'')

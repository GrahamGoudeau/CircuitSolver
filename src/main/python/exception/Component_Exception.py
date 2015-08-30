from Error import Error


# camelCase to conform with Python-style exceptions
class UnknownComponentError(Error):
    def __init__(self):
        super(UnknownComponentError, self)\
            .__init__('Unrecognized component type')


# takes a uuid to generate the exception message
class UnrecognizedIdError(Error):
    def __init__(self, uuid):
        super(UnrecognizedIdError, self)\
            .__init__('Unrecognized id: \'' + str(uuid) + '\'')

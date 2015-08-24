class Error(Exception):
    pass

class UnknownComponentError(Error):
    def __init__(self, msg):
        super(UnknownComponentError, self).__init__(msg)

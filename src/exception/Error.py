class Error(Exception):
    def __init__(self, msg):
        super(Error, self).__init__(msg)

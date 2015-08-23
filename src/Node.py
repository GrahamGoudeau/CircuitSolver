###############################################################################
class Node(object):
    """
    An object that can connect to any other object in a circuit
    """
    ###########################################################################
    def __init__(self, id):
        """
        DESCRIPTION
            Constructor for Node
        PARAMETERS
            id, int, required
                This is the unique id of the Node so that it can be 
                identified
        RETURNS
            New instance of a Node
        """
        self.id = id

    ###########################################################################
    def get_id(self):
        """
        DESCRIPTION
            Getter for id of Node
        PARAMETERS
            None
        RETURNS
            Unique id (int) of the node
        """
        return self.id

###############################################################################

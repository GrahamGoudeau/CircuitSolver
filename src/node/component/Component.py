import os
import sys
dirname = os.path.dirname(__file__)
'''
This is so the file can import from its parent directory;
Can use if running this file as a script:
if dirname == '':
    dirname = '.'
'''
sys.path.append(os.path.abspath(dirname + '/' + '../..'))

import node.Node as node


###############################################################################
class Component(node.Node):
    """
    An element of a circuit that affects the flow of current in some way, or
    serves some purpose other than connecting other components
    """
    ###########################################################################
    def __init__(self, id):
        """
        DESCRIPTION
            Constructor for a component
        PARAMETERS
            id, int, required
                Unique id of component
        RETURNS
            New instance of a component
        """
        super(Component, self).__init__(id)

###############################################################################

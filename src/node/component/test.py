import os
import sys
dirname = os.path.dirname(__file__)
if dirname == '':
    dirname = '.'
sys.path.append(os.path.abspath(dirname + '/' + '../..'))
print "done"

print __name__
print __file__
print __package__
print sys.path
import node
print node.Node
print node.__all__

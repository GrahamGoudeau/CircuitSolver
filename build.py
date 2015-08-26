from pybuilder.core import init
from pybuilder.core import use_plugin
from pybuilder.core import Author
from pybuilder.core import task

use_plugin('python.core')
use_plugin('python.flake8')
use_plugin('python.unittest')

# using the distutils pluging breaks the build, not sure why
# use_plugin('python.distutils')

name='CircuitSolver'
version='1.0.0'
authors=[Author('Graham Goudeau', 'grahamgoudeau@gmail.com'),
         Author('Ryan Gill')]

@init
def init(project):
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)

default_task = ['analyze', 'publish']

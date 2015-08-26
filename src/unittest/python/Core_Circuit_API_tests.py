import unittest
import os
import sys
import uuid

dirname = os.path.dirname(__file__)
if dirname == '':
    dirname = '.'

sys.path.append(os.path.abspath(dirname + '/' + '../../../'))

import src.Circuit as Circuit
import src.node.Node as Node
import src.Component_Types as Component_Types

class TestCoreCircuitAPIMethods(unittest.TestCase):
    def setUp(self):
        self.circuit = Circuit.Circuit()

    def tearDown(self):
        self.circuit = None

    def test_init(self):
        self.assertEqual(len(self.circuit.node_map.keys()), 0)

    def add_resistor(self, resistance):
    def test_add_node(self):
        resistor = Component_Types.Two_Prong_Component_Types.RESISTOR
        j1, j2 = self.circuit.add_two_prong_component(resistor, 50)
        self.assertTrue(isinstance(j1, uuid.UUID))
        self.assertTrue(isinstance(j2, uuid.UUID))
        self.assertEqual(len(self.circuit.node_map.keys()), 3)

if __name__ == '__main__':
    unittest.main()

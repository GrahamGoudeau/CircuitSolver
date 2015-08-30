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
import src.exception.Component_Exception as Component_Exception


class TestCoreCircuitAPIMethods(unittest.TestCase):
    def setUp(self):
        self.circuit = Circuit.Circuit()

    def tearDown(self):
        self.circuit = None

    def get_len_keys(self):
        return len(self.circuit.node_map.keys())

    def test_init(self):
        self.assertEqual(self.get_len_keys(), 0)

    def test_add_single_node(self):
        node = Node.Node(uuid.uuid4())
        self.circuit.add_node_to_map(node)
        self.assertEqual(self.get_len_keys(), 1)

    def test_add_multiple_nodes(self):
        node1 = Node.Node(uuid.uuid4())
        node2 = Node.Node(uuid.uuid4())
        node3 = Node.Node(uuid.uuid4())

        self.circuit.add_nodes_to_map([node1, node2, node3])
        self.assertEqual(self.get_len_keys(), 3)

    def test_valid_retrieve_node(self):
        id = uuid.uuid4()
        node = Node.Node(id)
        self.circuit.add_node_to_map(node)

        retrieve = self.circuit.get_node(id)
        self.assertEqual(node, retrieve)

    def test_invalid_retrieve_node_nonexistent(self):
        # invalid id
        retrieve = self.circuit.get_node(-1)
        self.assertEqual(retrieve, None)

    def test_invalid_retrieve_node_deleted(self):
        id = uuid.uuid4()
        node = Node.Node(id)
        self.circuit.add_node_to_map(node)

        self.circuit.remove_node_from_map(id)

        retrieve = self.circuit.get_node(id)
        self.assertEqual(retrieve, None)

    def test_valid_delete_node(self):
        id = uuid.uuid4()
        node = Node.Node(id)

        self.circuit.add_node_to_map(node)
        deleted = self.circuit.remove_node_from_map(id)
        self.assertEqual(deleted, node)

        retrieve = self.circuit.get_node(id)
        self.assertEqual(retrieve, None)

    def test_invalid_delete_nonexistent(self):
        retrieve = self.circuit.remove_node_from_map(-1)
        self.assertEqual(retrieve, None)

    def test_invalid_delete_repeated(self):
        id = uuid.uuid4()
        node = Node.Node(id)

        self.circuit.add_node_to_map(node)
        deleted = self.circuit.remove_node_from_map(id)
        self.assertEqual(deleted, node)

        repeat_deleted = self.circuit.remove_node_from_map(id)
        self.assertEqual(repeat_deleted, None)

    def test_connection_junction_to_node(self):
        j1, j2, resistor_id1 = self.add_resistor(50)
        j3, j4, resistor_id2 = self.add_resistor(100)

        resistor2 = self.circuit.get_node(resistor_id2)

        self.circuit.connect_junction_to_node(j2, resistor2)

        junction2 = self.circuit.get_node(j2)

        self.assertTrue(resistor2 in junction2.connections)

    def test_invalid_connection_junction_to_node(self):
        j1, j2, resistor_id = self.add_resistor(50)

        resistor_object = self.circuit.get_node(resistor_id)

        with self.assertRaises(Component_Exception.UnrecognizedIdError):
            self.circuit.connect_junction_to_node(-1, resistor_object)

    def test_combine_junctions(self):
        j1, j2, id = self.add_resistor(50)

        resistor_object = self.circuit.get_node(id)

        self.circuit.combine_junctions(j1, j2)

        self.assertEqual(resistor_object.junctionA, resistor_object.junctionB)

    def test_both_invalid_combine_junctions(self):
        with self.assertRaises(Component_Exception.UnrecognizedIdError):
            self.circuit.combine_junctions(uuid.uuid4(), uuid.uuid4())

    def test_one_invalid_combine_junctions(self):
        j1, _, _ = self.add_resistor(50)

        with self.assertRaises(Component_Exception.UnrecognizedIdError):
            self.circuit.combine_junctions(j1, uuid.uuid4())

    def add_resistor(self, resistance):
        resistor = Component_Types.Two_Prong_Component_Types.RESISTOR

        # add a new resistor, not connected to anything
        j1, j2 = self.circuit.add_two_prong_component(resistor, resistance)

        # return the id of the newly created resistor, which we
        # can get because we know it is the only connection
        # on the new junctions
        junction1 = self.circuit.get_node(j1)
        resistor_object_id = junction1.connections[0].get_id()
        return (j1, j2, resistor_object_id)

if __name__ == '__main__':
    unittest.main()

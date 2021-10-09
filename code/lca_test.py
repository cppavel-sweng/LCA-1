from lca import LCA, Node
from parameterized import parameterized, parameterized_class

import logging
import unittest


class LcaTest(unittest.TestCase):
    """Test Class for lca.py.

         Uses parameterized testing and coverage collection. 
         Larger objects are logged into a separate file, for example arrays, 
         which take part in the assert statements.

         This log file can be viewed after the tests are run, since it is opened with the
         "more" command.

         This project assumes you are running on windows. If you have docker installed 
         all you need to do is open cmd and run run_tests.cmd to execute tests.

         On mac/linux, you may have to copy the commands from run_tests.cmd, tweak them a little 
         bit and run them in terminal.

         The current version coverage is 100% (feel free to verify it yourself by running tests).
    """

    def setUp(self):

        # Valid tree:
        """
                                1
                               / \
                              2   3
                             / \ / \
                            4  5 6  7
                              /      \
                             8        9
                                     /
                                    10
        """
        self.valid_tree = Node(1)
        self.valid_tree.left = Node(2)
        self.valid_tree.right = Node(3)
        self.valid_tree.left.left = Node(4)
        self.valid_tree.left.right = Node(5)
        self.valid_tree.right.left = Node(6)
        self.valid_tree.right.right = Node(7)
        self.valid_tree.left.right.left = Node(8)
        self.valid_tree.right.right.right = Node(9)
        self.valid_tree.right.right.right.left = Node(10)

        # Empty tree

        self.empty_tree = None

        # Tree only consisting of root

        self.only_root = Node(1)

        # Set up logging
        logging.basicConfig(filename="lca_test.log",
                            encoding="utf-8", level=logging.INFO)

    @parameterized.expand([
        ("left subtree", 4, True, [1, 2, 4]),
        ("right subtree", 9, True, [1, 3, 7, 9]),
        ("root", 1, True, [1]),
        ("deepest left", 8, True, [1, 2, 5, 8]),
        ("deepest right", 10, True, [1, 3, 7, 9, 10]),
        ("non-existent", 228, False, []),
    ])
    def test_valid_find_path(self, name, node_id, expected, expected_path):
        actual_path = []
        self.assertEqual(expected, LCA.find_path(
            self.valid_tree, node_id, actual_path))
        logging.info(f"actual path in the tree is {actual_path} for test with name: {name} "
                     f"and destination node: {node_id}")
        self.assertListEqual(expected_path, actual_path)

    @parameterized.expand([
        ("non-existent", 2, False, []),
    ])
    def test_empty_find_path(self, name, node_id, expected, expected_path):
        actual_path = []
        self.assertEqual(expected, LCA.find_path(
            self.empty_tree, node_id, actual_path))
        logging.info(f"actual path in the tree is {actual_path} for test with name: {name} "
                     f"and destination node: {node_id}")
        self.assertListEqual(expected_path, actual_path)

    @parameterized.expand([
        ("non-existent", 2, False, []),
        ("root", 1, True, [1]),
    ])
    def test_root_find_path(self, name, node_id, expected, expected_path):
        actual_path = []
        self.assertEqual(expected, LCA.find_path(
            self.only_root, node_id, actual_path))
        logging.info(f"actual path in the tree is {actual_path} for test with name: {name} "
                     f"and destination node: {node_id}")
        self.assertListEqual(expected_path, actual_path)

    @parameterized.expand([
        ("left subtree-lca", 4, 8, 2),
        ("right subtree-lca", 10, 6, 3),
        ("same node", 7, 7, 7),
        ("left and right child of the same node", 6, 7, 3),
        ("root with some other node", 1, 10, 1),
    ])
    def test_valid_lca(self, name, node_1, node_2, expected):
        self.assertEqual(expected, LCA.find_LCA(
            self.valid_tree, node_1, node_2))

    @parameterized.expand([
        ("arbitrary", 55, 99, -1),
        ("root with itself", 1, 1, -1),
        ("same node", 7, 7, -1),
    ])
    def test_empty_lca(self, name, node_1, node_2, expected):
        self.assertEqual(expected, LCA.find_LCA(
            self.empty_tree, node_1, node_2))

    @parameterized.expand([
        ("arbitrary", 10, 1, -1),
        ("root with itself", 1, 1, 1),
        ("same node", 7, 7, -1),
        ("root with other node", 1, 99, -1),
    ])
    def test_only_root_lca(self, name, node_1, node_2, expected):
        self.assertEqual(expected, LCA.find_LCA(
            self.only_root, node_1, node_2))


if __name__ == "__main__":
    unittest.main(verbosity=2)

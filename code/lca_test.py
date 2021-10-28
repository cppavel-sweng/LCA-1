from lca import LCA, Node, DAG
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

        # DAG example for Wikipedia
        # https://en.wikipedia.org/wiki/Directed_acyclic_graph#/media/File:Tred-G.svg

        self.dag_example = DAG(
            [
            #      A     B       C     D      E
                [False, True,  True,  True,  True],   # A 
                [False, False, False, True,  False],  # B
                [False, False, False, True,  True],   # C 
                [False, False, False, False, True],   # D 
                [False, False, False, False, False]   # E
            ]
        )

        # DAG example from Baeldung
        # https://www.baeldung.com/wp-content/uploads/sites/4/2021/01/Dag-3.jpg

        self.dag_complex = DAG(
            [
            #      0      1     2      3      4       5      6      7      8
                [False, True,  True, False, False,  False, False, False, False], # 0 
                [False, False, False, False, True,  False, True,  False, False], # 1
                [False, False, False, True,  True,  False, True,  False, False], # 2 
                [False, False, False, False, False, False, True,  False, False], # 3 
                [False, False, False, False, False, False, False, False, False], # 4
                [False, False, False, False, False, False, False, False, False], # 5 
                [False, False, False, False, False, True,  False, True,  False], # 6 
                [False, False, False, False, False, False, False, False, True ], # 7 
                [False, False, False, False, False, False, False, False, False]  # 8
            ]
        )

        # DAG with multiple roots

        self.dag_multiple_roots = DAG(
            [
                # 0       1      2      3      4     5      6      7       8      9
                [False, False, False, False, False, False, False, True,  False, False ],  # 0
                [False, False, False, True,  False, False, False, False, False, False ],  # 1 
                [False, False, False, False, True,  False, False, True,  False, False ],  # 2 
                [False, False, False, False, False, True,  False, False, False, False ],  # 3
                [False, False, False, False, False, True,  True,  False, False, False ],  # 4
                [False, False, False, False, False, False, False, False, True,  True  ],  # 5
                [False, False, False, False, False, False, False, False, False, True  ],  # 6 
                [False, False, False, False, False, False, True,  False, False, False ],  # 7
                [False, False, False, False, False, False, False, False, False, False ],  # 8
                [False, False, False, False, False, False, False, False, False, False ],  # 9
            ]
        )

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
    def test_valid_find_path_binary(self, name, node_id, expected, expected_path):
        actual_path = []
        self.assertEqual(expected, LCA.find_path_binary(
            self.valid_tree, node_id, actual_path))
        logging.info(f"actual path in the tree is {actual_path} for test with name: {name} "
                     f"and destination node: {node_id}")
        self.assertListEqual(expected_path, actual_path)

    @parameterized.expand([
        ("non-existent", 2, False, []),
    ])
    def test_empty_find_path_binary(self, name, node_id, expected, expected_path):
        actual_path = []
        self.assertEqual(expected, LCA.find_path_binary(
            self.empty_tree, node_id, actual_path))
        logging.info(f"actual path in the tree is {actual_path} for test with name: {name} "
                     f"and destination node: {node_id}")
        self.assertListEqual(expected_path, actual_path)

    @parameterized.expand([
        ("non-existent", 2, False, []),
        ("root", 1, True, [1]),
    ])
    def test_root_find_path_binary(self, name, node_id, expected, expected_path):
        actual_path = []
        self.assertEqual(expected, LCA.find_path_binary(
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
    def test_valid_lca_binary(self, name, node_1, node_2, expected):
        self.assertEqual(expected, LCA.find_LCA_binary(
            self.valid_tree, node_1, node_2))

    @parameterized.expand([
        ("arbitrary", 55, 99, -1),
        ("root with itself", 1, 1, -1),
        ("same node", 7, 7, -1),
    ])
    def test_empty_lca_binary(self, name, node_1, node_2, expected):
        self.assertEqual(expected, LCA.find_LCA_binary(
            self.empty_tree, node_1, node_2))

    @parameterized.expand([
        ("arbitrary", 10, 1, -1),
        ("root with itself", 1, 1, 1),
        ("same node", 7, 7, -1),
        ("root with other node", 1, 99, -1),
    ])
    def test_only_root_lca_binary(self, name, node_1, node_2, expected):
        self.assertEqual(expected, LCA.find_LCA_binary(
            self.only_root, node_1, node_2))

    @parameterized.expand([
        ("dag-complex, arbitrary - 1", 4, [0, 1, 2]),
        ("dag-complex, arbitrary - 2", 7, [0, 1, 2, 3, 6]),
    ])
    def test_dfs_helper(self, name, dest, expected):
        parents = []
        LCA.dfs_helper(self.dag_complex, 0, dest, [], parents)
        self.assertCountEqual(parents, expected)


    @parameterized.expand([
        ("multiple roots", [0, 1, 2]),
    ])
    def test_find_all_roots(self, name,  expected):
        actual = LCA.find_all_roots(self.dag_multiple_roots)
        self.assertCountEqual(actual, expected)

    @parameterized.expand([
        ("arbitrary - 1", 3, 4, [1, 2]),                     # D, E -> C, B
        ("arbitrary - 2", 3, 2, [0]),                        # D, C -> A
        ("arbitrary - 3", 1, 4, [0]),                        # B, E -> A
        ("arbitrary - 3, change order", 4, 1, [0]),          # E, B -> A
        ("root with other node - 1", 0, 4, [0]),             # A, E -> A
        ("root with other node - 2", 4, 0, [0]),             # E, A -> A
        ("node with itself", 2, 2, [0]),                     # C, C -> A
    ])
    def test_valid_lca_dag_wiki(self, name, node_1, node_2, expected):
        self.assertCountEqual(expected, LCA.find_LCA_DAG(
            self.dag_example, node_1, node_2))

    @parameterized.expand([
        ("arbitrary - 1", 4, 7, [1, 2]),                        # 4,7 -> 1, 2
        ("arbitrary - 1 - change order", 7, 4, [1, 2]),         # 4,7 -> 1, 2
        ("root with other node - 1", 0, 8, [0]),                # 0,8 -> 0
        ("root with other node - 2", 8, 0, [0]),                # 8,0 -> 0          
        ("node with itself", 2, 2, [0]),                        # 2,2 -> 0                 
    ])
    def test_valid_lca_dag_complex(self, name, node_1, node_2, expected):
        self.assertCountEqual(expected, LCA.find_LCA_DAG(
            self.dag_complex, node_1, node_2))

    @parameterized.expand([
        ("root with another root", 0, 2, []),                   # 0,2 -> NO LCA
        ("simple - 1", 8, 9, [5]),                              # 8,9 -> 5
        ("multiple lcas", 5, 8, [3, 4]),                        # 5,8 -> 3, 4            
    ])
    def test_valid_lca_dag_multiple_roots(self, name, node_1, node_2, expected):
        self.assertCountEqual(expected, LCA.find_LCA_DAG(
            self.dag_multiple_roots, node_1, node_2))

if __name__ == "__main__":
    unittest.main(verbosity=2)

from dataclasses import dataclass
import typing


@dataclass
class Node:
    """Node class for the tree."""
    identifier: int
    left: typing.Any = None
    right: typing.Any = None

@dataclass
class DAG:
    adjacency_matrix: typing.List[typing.List[bool]]

class LCA:
    """Simple class that provides LCA functionality for binary trees."""
    @staticmethod
    def find_path_binary(root: typing.Type[Node],
                  id: int,
                  current_path: typing.List[Node]) -> bool:
        """Finds path from root to the node with specified id.

            Returns True if the path was found and False if there was no path found.
            Returns the modified current_path array which contains the path to the node (if found).
        """
        if root is None:
            return False

        current_path.append(root.identifier)
        if root.identifier == id:
            return True

        if ((root.left and LCA.find_path_binary(root.left, id, current_path))
                or (root.right and LCA.find_path_binary(root.right, id, current_path))):
            return True

        current_path.pop()
        return False

    @staticmethod
    def find_LCA_binary(root: typing.Type[Node],
                 id1: int,
                 id2: int) -> int:
        """Finds the least common ancestor for two nodes in a binary tree.

            Returns -1 if the lowest commmon ancestor does not exist.
        """
        path_1 = []
        path_2 = []

        if (not LCA.find_path_binary(root, id1, path_1)) or (not LCA.find_path_binary(root, id2, path_2)):
            return - 1

        i = 0
        while(i < len(path_1) and i < len(path_2)):
            if path_1[i] != path_2[i]:
                break
            i += 1
        return path_1[i-1]

    @staticmethod 
    def dfs_helper(graph: DAG, current: int, dest: int, path: typing.List[int], 
        parents: typing.List[int]):
        """Finds all parents of a particular node in DAG.

            Returns an array of all unique parents in parents parameter
        """
        if current == dest:
            for node in path:
                if node not in parents:
                    parents.append(node)

        path.append(current)
        
        for index in range(0, len(graph.adjacency_matrix[current])):
            if graph.adjacency_matrix[current][index]:
                LCA.dfs_helper(graph, index, dest, path, parents)
        
        path.pop()

    @staticmethod 
    def find_all_roots(graph: DAG) -> typing.List[int]:
        """Finds all roots (vertices with in_degree = 0).

            Returns list of unique roots
        """
        roots = []
        for j in range(0, len(graph.adjacency_matrix[0])):
            in_degree = 0
            for i in range(0, len(graph.adjacency_matrix)):
                if graph.adjacency_matrix[i][j]:
                    in_degree = in_degree + 1
                
            if in_degree == 0:
                roots.append(j)

        return roots

    @staticmethod
    def find_LCA_DAG(graph: DAG, a: int, b: int) -> int:
        """Finds all LCAs for a and b in the graph.

            Lowest common ancestors of x and y are the nodes of out-degree zero in the subgraph of G 
            induced by the set of common ancestors of x and y.

            Hence LCA(node, node) is a set of direct parents of node.

            This is different from binary tree definition where LCA(node, node) is considered to be node.

            I do not consider node to be part of the parents subgraph in case of DAGs.

            Returns an array of unique LCA indexes without any guaranteed order.
        """
        roots = LCA.find_all_roots(graph)
        lcas = []

        for root in roots:

            parents_of_a = []
            parents_of_b = []
            ## replace with finding roots
            LCA.dfs_helper(graph, root, a, [], parents_of_a)
            LCA.dfs_helper(graph, root, b, [], parents_of_b)

            if not parents_of_a:
                parents_of_a.append(a)

            if not parents_of_b:
                parents_of_b.append(b)

            intersection_of_parents = [value for value in parents_of_a if value in parents_of_b]

            for lca_candidate in intersection_of_parents:
                out_degree = 0
                for index in range(0, len(graph.adjacency_matrix[lca_candidate])):
                    if graph.adjacency_matrix[lca_candidate][index] and index in intersection_of_parents:
                        out_degree = out_degree + 1

                if out_degree == 0:
                    if lca_candidate not in lcas:
                        lcas.append(lca_candidate)

        return lcas
        

from dataclasses import dataclass
import typing


@dataclass
class Node:
    """Node class for the tree."""
    identifier: int
    left: typing.Any = None
    right: typing.Any = None


class LCA:
    """Simple class that provides LCA functionality for binary trees."""
    @staticmethod
    def find_path(root: typing.Type[Node],
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

        if ((root.left and LCA.find_path(root.left, id, current_path))
                or (root.right and LCA.find_path(root.right, id, current_path))):
            return True

        current_path.pop()
        return False

    @staticmethod
    def find_LCA(root: typing.Type[Node],
                 id1: int,
                 id2: int) -> int:
        """Finds the least common ancestor for two nodes in a binary tree.

            Returns -1 if the lowest commmon ancestor does not exist.
        """
        path_1 = []
        path_2 = []

        if (not LCA.find_path(root, id1, path_1)) or (not LCA.find_path(root, id2, path_2)):
            return - 1

        i = 0
        while(i < len(path_1) and i < len(path_2)):
            if path_1[i] != path_2[i]:
                break
            i += 1
        return path_1[i-1]

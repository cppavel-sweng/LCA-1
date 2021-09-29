import typing

class Node:
    """Node class for the tree."""
    def __init__(self, id):
        self.identifier = id
        self.left = None
        self.right = None

class LCA:
    """Simple class that provides LCA functionality for binary trees."""
    @staticmethod
    def find_path(root: typing.Type[Node] ,
                 id: int,
                 current_path: typing.List[Node]) -> bool:
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


def main():

  #TODO(cppavel-sweng): Add unit tests for this file

  """
                          1
                         / \
                        2   3
                       / \ / \
                      4  5 6  7
  """
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)
 
  print(f"LCA(4, 5) = {LCA.find_LCA(root, 4, 5)}")
  print(f"LCA(3, 4) = {LCA.find_LCA(root, 3, 4)}")
  print(f"LCA(4, 7) = {LCA.find_LCA(root, 4, 7)}")
  print(f"LCA(5, 3) = {LCA.find_LCA(root, 5, 3)}")
  print(f"LCA(6, 7) = {LCA.find_LCA(root, 6, 7)}")
  print(f"LCA(1, 2) = {LCA.find_LCA(root, 1, 2)}")
  print(f"LCA(1, 1) = {LCA.find_LCA(root, 1, 1)}")

if __name__=="__main__":
    main()
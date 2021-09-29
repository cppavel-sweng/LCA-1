class TreeNode{
    public left: TreeNode|undefined;
    public right: TreeNode|undefined;
    public id: number;
    constructor(id:number) {
    this.id = id;
  }
}
class LCA{
    static find_path(root: TreeNode, id: number, current_path: number[]): boolean{
       if (root == null){
           return false;
       }
       current_path.push(root.id);

       if (root.id == id)
       {
           return true;
       }

       if ((root.left != null && LCA.find_path(root.left, id, current_path)) || 
            (root.right != null && LCA.find_path(root.right, id, current_path))){
                return true;
            }
       
       current_path.pop()

       return false;
    }

    static find_LCA(root: TreeNode, id1: number, id2: number):number{
        let path_1: number[] = [];
        let path_2: number[] = [];

        if (!LCA.find_path(root, id1, path_1) || !LCA.find_path(root, id2, path_2)){
            return -1;
        }

        let i: number  = 0
        while(i < path_1.length && i < path_2.length)
        {
            if (path_1[i] != path_2[i])
            {
                break;
            }
            i = i + 1;
        }
        return path_1[i-1]
        
    }
}

let root:TreeNode  = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3)
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(7);

console.log("LCA (2, 7): "+ LCA.find_LCA(root, 2, 7));
console.log("LCA (2, 3): "+ LCA.find_LCA(root, 2, 3));
console.log("LCA (3, 4): "+ LCA.find_LCA(root, 4, 5));
console.log("LCA (6, 7): "+ LCA.find_LCA(root, 6, 7));
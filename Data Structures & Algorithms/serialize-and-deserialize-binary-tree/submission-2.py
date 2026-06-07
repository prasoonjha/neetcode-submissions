# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def construct(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = preorder.pop(0)
        root_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.construct(preorder, inorder[:root_idx])
        root.right = self.construct(preorder, inorder[root_idx+1:])
        return root
    
    
            
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
    
    

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        encoded = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if encoded[i] == "N":
                i+=1
                return None
            root = TreeNode(int(encoded[i]))
            i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        
        

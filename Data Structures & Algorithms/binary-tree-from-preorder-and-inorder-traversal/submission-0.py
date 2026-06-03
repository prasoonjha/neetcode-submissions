# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def buildTreeHelper(self, root: Optional[TreeNode], preorder: List[int], inorder: List[int]) ->
    #         """
    #          function that takes the root, preorder and inorder list and 
    #         updates root recursively returns None
    #         The math relies on the fact that the size of the left subtree 
    #         is the same in both lists. If the root is at inorder_idx, then 
    #         there are exactly inorder_idx nodes in the left subtree. You use
    #          this count to slice the preorder list: preorder[1 : 1 + inorder_idx]
    #           for the left and preorder[1 + inorder_idx :] for the right.
    #         return: None
    #         """

        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we are given inorder and preorder traversals as list
        # we want to make the tree. start with the root node
        """
        preorder: NLR
        inorder: LNR   
            updates root recursively 
            The math relies on the fact that the size of the left subtree 
            is the same in both lists. If the root is at inorder_idx, then 
            there are exactly inorder_idx nodes in the left subtree. You use
             this count to slice the preorder list: preorder[1 : 1 + inorder_idx]
              for the left and preorder[1 + inorder_idx :] for the right.
            return: None
        
        """
        if not inorder: return None

        root_val = preorder.pop(0) #neat trick
        root_idx = inorder.index(root_val)
        root = TreeNode(root_val)

        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx+1:])
        
        return root


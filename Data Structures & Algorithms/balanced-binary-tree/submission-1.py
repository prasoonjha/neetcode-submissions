# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Here’s a more efficient pattern: return -1 if unbalanced.
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            lh = dfs(node.left)
            if lh == -1:
                return -1
            
            rh = dfs(node.right)
            if rh == -1:
                return -1
            
            if abs(lh - rh) > 1:
                return -1
            
            return 1 + max(lh, rh)
        
        return dfs(root) != -1
"""
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        return height along with isBalanced for every node
        """
        def dfs(root):
            if not root:
                return True, 0
            isLeftBalanced, lh = dfs(root.left)
            isRightBalanced, rh = dfs(root.right)
            if (not isLeftBalanced) or (not isRightBalanced) or (abs(lh-rh) >1):
                print(f"{root.val=}{isLeftBalanced=}{isRightBalanced=}")
                return False, 1+max(lh, rh)
            
            return True, 1+max(lh, rh)
        isBalanced, height = dfs(root)
        return isBalanced
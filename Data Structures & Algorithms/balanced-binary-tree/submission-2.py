# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = False
        def dfs(root):
            if not root:
                return (0, True)

            lh, isLeftBalanced = dfs(root.left)
            rh, isRightBalanced = dfs(root.right)
            return 1+max(lh, rh),  isLeftBalanced and isRightBalanced and abs(lh-rh)<=1
        _, isBalanced = dfs(root)
        return isBalanced
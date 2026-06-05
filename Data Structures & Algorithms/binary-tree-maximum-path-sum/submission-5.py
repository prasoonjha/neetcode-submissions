# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            ls = dfs(root.left)
            rs = dfs(root.right)
            max_sum =max(max_sum, max(ls, 0)+max(rs, 0)+root.val)
            return root.val+max(max(ls, 0),max(rs, 0))
        dfs(root)
        return max_sum
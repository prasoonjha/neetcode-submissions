# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root: return 0
            l_sum = dfs(root.left)
            r_sum = dfs(root.right)
            opt1 = root.val+max(l_sum, r_sum)
            opt2 = root.val+max(l_sum, 0)+max(r_sum,0)
            res= max(res, opt1, opt2)
            return max(root.val, opt1)
        dfs(root)
        return res
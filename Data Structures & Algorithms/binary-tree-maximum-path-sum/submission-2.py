# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')
        def dfs(root):
            nonlocal res 
            if not root: return 0
            max_path_sum_left = dfs(root.left)
            max_path_sum_right = dfs(root.right)

            #option 1:connect parent to max of left, right
            sum_if_keep_parent = root.val + max(max_path_sum_left, max_path_sum_right)
            #option 2: disconnect parent to max
            sum_if_disconnect_parent = root.val + max(max_path_sum_left, 0) + max(max_path_sum_right, 0)
            res = max(res, sum_if_keep_parent, sum_if_disconnect_parent)
            return max(root.val, sum_if_keep_parent)
        dfs(root)
        return res
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        root, p, q
        5, 3, 5
        """
        def dfs(r, p, q):
            if not r:
                return None
            if p.val == r.val or q.val == r.val:
                return r
            if p.val < r.val < q.val or q.val < r.val < p.val:
                return r
            left =  dfs(r.left, p, q)
            right = dfs(r.right, p, q)
            return r if (left and right) else (left or right)
            
        return dfs(root, p, q)

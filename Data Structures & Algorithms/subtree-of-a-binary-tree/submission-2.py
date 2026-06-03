# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        if (not p) or (not q):
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        return p.val == q.val and l and r
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r
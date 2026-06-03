# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return
        if (root.left == None and root.right == None):
            return root
        left = root.left
        right = root.right
        leftInverted = self.invertTree(left)
        rightInverted = self.invertTree(right)
        root.right = leftInverted;
        root.left = rightInverted;
        return root

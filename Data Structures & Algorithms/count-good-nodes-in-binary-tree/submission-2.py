# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, _max):
            nonlocal count
            if not root:
                return
            _max = max(root.val, _max)
            print(f"{root.val=}{_max=}")
            if root.val>=_max:
                count+=1
            dfs(root.left,_max)
            dfs(root.right, _max)
            
            
        dfs(root, root.val)
        return count
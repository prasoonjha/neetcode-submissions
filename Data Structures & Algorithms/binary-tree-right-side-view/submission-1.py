# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        dfs solution. 
        for each level, track h and index, for root 0, 0
        r.right -> 1,1
        r.left -> 1,-1

        we can solve it using bfs as well
        """
        res = []
        levels = defaultdict(list)
        def dfs(root, h, idx):
            if not root:
                return
            levels[h].append((root.val, h, idx))       
            dfs(root.left, h+1, idx-1)
            dfs(root.right, h+1, idx+1) 

        dfs(root, 0, 0)
        for k, v in levels.items():
            res.append(v[-1][0])
        return res
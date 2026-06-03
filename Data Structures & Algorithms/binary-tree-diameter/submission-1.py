class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        we do a postorder dfs to return the diameter of the binary tree
        before processing current node,we need to know the diameter
        of the left and right child
        then we have 2 options, we keep the max(detach from parent, 
        continue increasing parent's length)
        """
        dmtr = 0
        def dfs(root):
            nonlocal dmtr
            if not root:
                return 0
            l_d = dfs(root.left)
            r_d = dfs(root.right)
            #detach from parent 
            opt_1 = l_d+r_d
            #or continue
            opt_2 = max(l_d,r_d)
            dmtr = max(dmtr, opt_1)
            #always return the result from opt2 to support recursion
            return 1+opt_2
        dfs(root)
        return dmtr
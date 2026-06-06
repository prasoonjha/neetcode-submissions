class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(curr, numOpen, numClose):
            if numClose == 0 and numOpen == 0:
                res.append(curr)
                return
            if numClose>numOpen:
                dfs(curr+")", numOpen, numClose-1)
            if numOpen>0:
                dfs(curr+"(", numOpen-1, numClose)
        dfs("", n, n)
        return res
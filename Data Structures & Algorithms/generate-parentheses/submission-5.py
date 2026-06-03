class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        remaining = n
        def dfs(_open,_close, curr):
            if _open+_close == 0:
                res.append(curr)
                return
            if _open>0:
                dfs(_open-1,_close, curr+"(")
            if _close>_open:
                dfs(_open, _close-1, curr+")")
            
        dfs(n, n, "")
        return res
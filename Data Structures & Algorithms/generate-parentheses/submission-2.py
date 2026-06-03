class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")": "(", "}": "{", "]": "["}
        stack = deque([])
        for c in s:
            if c in valid and len(stack):
                #c is closing bracket
                top = stack[-1]
                if top != valid[c]:
                    return False
                stack.pop()
            else:
                #c is opening bracket
                stack.append(c)

        return True if len(stack) == 0 else False

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        remaining = n
        def dfs(_open,_close, curr):
            if _open+_close == 0:
                if _open == _close and self.isValid(curr):
                    res.append(curr)
                return
            dfs(_open-1,_close, curr+"(")
            if len(curr):
                dfs(_open, _close-1, curr+")")
            
        dfs(n, n, "")
        return res
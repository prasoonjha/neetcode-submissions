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
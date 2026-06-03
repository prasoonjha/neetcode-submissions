class Solution:
    def isValid(self, s: str) -> bool:
        isValid = False
        dict = {"(": ")","{":"}", "[":"]"}
        stack = []
        for c in s:   
            if c in dict:
                #if char is an opening bracket
                stack.append(c)
            else:
                #char is a closing bracket
                if len(stack) != 0:
                    #check top of stack
                    top = stack[-1]
                
                    #if top of stack is matching pair, pop 
                    if dict[top] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        if len(stack) == 0:
            isValid = True
        
        return isValid

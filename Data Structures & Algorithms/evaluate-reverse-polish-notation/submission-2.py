class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        The concept of a stack, a last-in/first-out construct, is integral to
        the left-to-right evaluation of RPN. In the example 3 4 -, first the 3
         is put onto the stack, then the 4; the 4 is now on top and the 3 below it.
          The subtraction operator removes the top two items from the stack, performs
           3 − 4, and puts the result of −1 onto the stack.
        """
        stack = deque([])
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                #operator, pop last two nums and perform operation, push result into stack
                a = stack.pop()
                b = stack.pop()
                
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(b-a)
                elif token == "/":
                    stack.append(int(b/a))
                else:
                    stack.append(a*b)

                print(f"{stack=}")

            else:
                #number, push into stack
                stack.append(int(token))
                print(f"{stack=}")
        return stack.pop()


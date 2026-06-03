class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        #add index to stack
        stack = deque([])
        res = [0]*n
        for i in range(n):
            temp_today = temperatures[i]
            while stack and (temperatures[stack[-1]]<temp_today):
                #pop
                diff= i-stack[-1]
                temp = stack.pop()
                res[temp] = diff
            stack.append(i)
        return res
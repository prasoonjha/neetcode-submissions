from collections import deque
class Solution:
    """
    [7,1,7,2,2,4]
    [0]
    [] -> 0
    0: curr_height

    if for any rectangle i know the immediate next smaller, the immediate previous smaller
    can i figure out what contribution will the index have in the answer
    if i figure it out for all indices, i can returnt the max area
    pl = [-1,-1,1,1, ]
    #stack can give me
    """
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        stack = deque()
        start, area = 0, 0
        pl = [-1]*n #initialize with -1
        nl = [n]*n #initialize with n so that area formula is valid

        for end in range(n-1, -1, -1):
            curr_height = heights[end]
            while stack and curr_height<heights[stack[-1]]:
                top = stack.pop()
                pl[top] = end
            stack.append(end)
        #reset queue
        stack = deque()
        for end in range(n):
            curr_height = heights[end]
            while stack and curr_height<heights[stack[-1]]:
                top = stack.pop()
                nl[top] = end
            stack.append(end)
        
        
        for i in range(n):
            L, R = pl[i], nl[i]
            
            if R == -1:
                R = n
            current_area = heights[i]*(R-L-1)
            area = max(area,current_area)
        return area
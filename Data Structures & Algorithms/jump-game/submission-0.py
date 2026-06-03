class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1
        for i in range(n-2, -1, -1):
            if i+nums[i]>=goal:
                goal = i
        return goal ==0




        # def dfs(i):
        #     if i==n-1:
        #         return True
        #     maxDistFromHere = nums[i]
        #     for j in range(i+1, i)

        # return dfs(0)
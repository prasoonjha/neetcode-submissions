class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            #num could be +ve or -ve. if +ve, current_max+nums[i], if -ve
            current_max = max(nums[i], current_max+nums[i])
            max_sum = max(max_sum, current_max)
        return max_sum
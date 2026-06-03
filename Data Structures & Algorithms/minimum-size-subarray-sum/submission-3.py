class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_size = float('inf')
        start = 0
        window_sum = 0
        for end in range(n):
            window_sum += nums[end] 
            while window_sum >= target:
                min_size = min(min_size, end-start+1)
                #shrink from start
                window_sum -= nums[start]
                start+=1   
                
            
        return 0 if min_size == float("inf") else min_size
            
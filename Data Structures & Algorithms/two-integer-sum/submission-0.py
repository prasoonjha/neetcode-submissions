class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target-num
            if diff in dict:
                return [dict[diff], i] 
            else:
                dict[num] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen:
                if i<seen[target-num]:
                    return [i, seen[target-num]]
                else:
                    return [seen[target-num], i]
            seen[num] = i
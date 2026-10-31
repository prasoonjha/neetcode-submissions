class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set(nums)
        return len(_set) != len(nums)

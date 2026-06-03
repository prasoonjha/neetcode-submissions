class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        _prefix = [nums[0]]*n
        _suffix = [nums[n-1]]*n
        for i in range(1,n):
            _prefix[i] = _prefix[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            _suffix[i] = _suffix[i+1]*nums[i]
        prefix = ([1]+_prefix+[1])
        suffix = ([1]+_suffix+[1])
        n = len(prefix)
        res = []
        for i in range(1,n-1):
            res.append(prefix[i-1]*suffix[i+1])
        return res
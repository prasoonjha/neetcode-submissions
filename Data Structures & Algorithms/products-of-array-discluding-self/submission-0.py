class Solution:
    """
    nums =   [1,2,4,6]
    prefix = [1,2,8,48]
    suffix = [48,48,24,6]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        curr_prod = 1
        for i in range(n):
            curr_prod *= nums[i]
            prefix[i] = curr_prod
        curr_prod = 1
        for j in range(n-1,-1,-1):
            curr_prod *= nums[j]
            suffix[j] = curr_prod
        res = [1]*n
        for i in range(n):
            prod = 1
            #index ==0, res[0]=suffix
            if i == 0:
                prod = 1*suffix[i+1]
            if i>0 and i<n-1:
                prod = prefix[i-1]*suffix[i+1]
            if i == n-1:
                prod = prefix[i-1]
            res[i] = prod
        # print(prefix)
        # print(suffix)
        return res
class Solution:
    """
    houses are arranged in a circle?
    hmm..what does that mean, 
    what is the state, index i

    brute force, for each possible start i, caculate amt
    d
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)
        dp1 = [0]*(n-1) #dp array for robbery starting from 0:n-2
        dp2 = [0]*(n-1) #dp array for robbery starting from house 1:n-1

        #for index in case 1
        for i in range(0, n-1):
            if i == 0:
                dp1[i] = nums[0]
                continue
            if i == 1:
                dp1[i] = max(nums[i], nums[i-1] )
            dp1[i] = max(dp1[i-1], nums[i]+dp1[i-2])

        #for index in case 2
        for i in range(1, n):
            if i == 1:
                dp2[i-1] = nums[1]
                continue
            if i == 2:
                dp2[i-1] = max(nums[i], nums[i-1])
            dp2[i-1] = max(dp2[i-2], nums[i]+dp2[i-3])
        max_amt = max(max(dp1), max(dp2))
        return max_amt
class Solution:
    def isIS(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            curr_num = nums[i]
            next_num = nums[i+1]
            if curr_num<next_num:
                continue
            else:
                return False
        return True

    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        for each possible end of list,
        check what is the longest possible subsequence ending here
        store it
        do we need more than 
        """
        n = len(nums)
        
        subsequences = []
        curr = []
        res = -float("inf")
        def dfs(i, curr):
            nonlocal res
            if i == n:
                valid = []
                if self.isIS(curr):
                    subsequences.append(curr)
                    res = max(res, len(curr))
                return
            #left child pick ith number,
            dfs(i+1, curr+[nums[i]])
            #right child dont pick ith number
            dfs(i+1, curr)
        dfs(0, curr)
        
        return res
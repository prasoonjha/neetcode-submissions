class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subsets = []
        curr = []
        n = len(nums)
        sum_nums = sum(nums)
        print(sum_nums)
        def dfs(i, curr):
            if i == n:
                subsets.append(curr)
                
                return
            #dont pick ith num
            dfs(i+1, curr)
            #pick ith num
            dfs(i+1, curr+[nums[i]])
            
        dfs(0, curr)
        for subset in subsets:
            if 2*sum(subset) == sum_nums:
                    return True
        return False
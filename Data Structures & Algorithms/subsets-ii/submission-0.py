class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,1] -> [1,1,2]
                        []
                        /\
                       [1][]
                   /   \    /   \
                [1,1] [1]  [1]      []
                /\     /\       /\    /\
        [1,1,2][1,1] [1,2][1][1,2][1][2][]

        in which order should dfs be called, LRN or NLR??
        """
        res = set()
        n = len(nums)
        nums.sort()
        curr = []
        def dfs(i, curr):
            nonlocal res
            #base case
            if i==n:
                res.add(tuple(curr))
                return
            #dfs call left child pick nums[i]
            dfs(i+1, curr+[nums[i]])
            #right child doesnt pick nums[i]
            dfs(i+1, curr)
            
        dfs(0, curr)
        return list(res)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(start, remaining, curr):
            """
            start     → smallest index we are allowed to use
            remaining → how much sum is still needed
            curr      → current combination being built
            """

            # Base case: exact sum achieved
            if remaining == 0:
                # We found ONE valid combination
                # copy() is required because curr is mutable
                res.append(curr.copy())
                return

            # Try all choices starting from `start`
            for i in range(start, n):

                # Prune: this number is too large to fit
                if nums[i] > remaining:
                    continue

                # Choose nums[i]
                # - i (not i+1): reuse is allowed
                # - start ensures we never go backwards → no permutations
                dfs(
                    i,                          # reuse allowed
                    remaining - nums[i],        # reduce remaining sum
                    curr + [nums[i]]             # extend current path
                )

        # Start DFS from index 0 with full target
        dfs(0, target, [])

        return res

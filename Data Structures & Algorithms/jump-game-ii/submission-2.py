class Solution:
    def jump(self, nums: List[int]) -> int:
        # Length of the array
        n = len(nums)
        
        # The goal is to reach the last index
        goal = n - 1

        # Use memoization (cache) to avoid recomputing results
        cache = {}
        # Initialize minimum steps as infinity
        minSteps = float('inf')
        def dfs(i):
            nonlocal minSteps
            if i in cache:
                return cache[i]
            # Base case: if we are already at the last index
            if i == goal:
                return 0  # No more jumps needed
            
            # Determine the farthest index we can jump to from i
            end = min(goal, i + nums[i])

            

            # Try all possible jumps from i → (i+1 to end)
            for j in range(i + 1, end + 1):
                # Recursively compute minimum jumps from position j
                minSteps = min(minSteps, dfs(j))

            # Add 1 jump (current move) + best result from next positions
            cache[i] = 1+minSteps
            return 1 + minSteps

        # Start DFS from index 0
        return dfs(0)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        we can reach the nth index from n-1th or n-2th idx
        we will maintain a dp array of length n which will store the min cost to reach the ith stair

        """
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[n]
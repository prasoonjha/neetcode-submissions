class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #for any change i, min(dp[i-1])
        """
        for each coin, check how many coins will it take to reach sum of target amt
        for each coin in coins:
            
        """
        cache = {}
        def dfs(amount):

            #if amt <=0, return 0
            if amount == 0:
                return 0 
            
            if amount in cache:
                return cache[amount]
            ans = float('inf')
            for coin in coins:
                #for each coin, the min number of coins required to make 
                #amt is the min number of coins required to make 
                if amount-coin>=0:
                    ans = min(ans, 1+dfs(amount-coin))
            cache[amount] = ans      
            
            return ans
        ans = dfs(amount)
        return ans if ans != float('inf') else -1       

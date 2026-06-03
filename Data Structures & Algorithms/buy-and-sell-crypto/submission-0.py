class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        for sell in range(1,len(prices)):
            cp = prices[buy] #cost price
            sp = prices[sell] #sell price

            #keep cp as low as possible throughout iteration
            if sp < cp:
                buy = sell
            
            max_profit = max(max_profit, sp-cp)
            
            

        return max_profit
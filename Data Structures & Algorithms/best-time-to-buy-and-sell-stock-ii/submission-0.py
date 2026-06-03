class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(1, n):
            prev_price = prices[i-1]
            curr_price = prices[i]
            if curr_price>prev_price:
                max_profit+=curr_price-prev_price
        return max_profit
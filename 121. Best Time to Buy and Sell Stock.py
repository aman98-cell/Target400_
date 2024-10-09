from typing import List
prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if min_price > price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
                
        return max_profit
instance1 = Solution()
print(instance1.maxProfit(prices))




from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            elif prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
        return profit

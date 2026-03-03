#
# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# URL: https://neetcode.io/problems/buy-and-sell-crypto
# Date: 2026-03-02
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        best_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if best_profit < profit:
                best_profit = profit

            if profit < 0:
                l = r
            r += 1

        return best_profit

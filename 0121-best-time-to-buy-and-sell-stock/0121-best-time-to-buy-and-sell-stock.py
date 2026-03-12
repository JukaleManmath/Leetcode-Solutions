class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float("inf")
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] > buy:
                profit = max(profit, prices[i] - buy)
        return profit
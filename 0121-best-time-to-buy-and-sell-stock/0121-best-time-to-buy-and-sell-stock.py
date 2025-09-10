class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0
        curr = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] > buy:
                curr = prices[i] - buy
                if curr > profit:
                    profit = curr
        return profit

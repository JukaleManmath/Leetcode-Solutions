class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0
        for i in prices:
            if i < buy:
                buy = i
            if i > buy:
                profit += i - buy
                buy = i
        return profit
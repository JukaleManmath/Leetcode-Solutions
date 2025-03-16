class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxprofit = 0
        minsofar = prices[0]
        for i in range(len(prices)):
            minsofar = min(minsofar , prices[i])
            if prices[i] > minsofar:
                maxprofit = max(maxprofit , prices[i] - minsofar)
        return maxprofit
                


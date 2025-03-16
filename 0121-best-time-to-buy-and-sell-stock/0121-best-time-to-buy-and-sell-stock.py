class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minsofar = prices[0]
        for i in range(len(prices)):
            curr_profit = 0
            if(prices[i] > minsofar):
                curr_profit = prices[i] - minsofar
            maxprofit = max(maxprofit , curr_profit)
            minsofar = min(minsofar , prices[i])
        return maxprofit
                


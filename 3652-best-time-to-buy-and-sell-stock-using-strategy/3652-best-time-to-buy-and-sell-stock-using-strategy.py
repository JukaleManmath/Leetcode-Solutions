class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        ps = []
        ss = []
        for i in range(n):
            ps.append(ps[-1] + prices[i]) if ps else ps.append(prices[i])
            ss.append(ss[-1] + (prices[i] * strategy[i])) if ss else ss.append(prices[i] * strategy[i])
        
        profit = ss[-1]
        i , j = 0 , k - 1
        while j < n:
            curr_profit = 0
            if i > 0:
                curr_profit += ss[i-1]
            mid = (j - i + 1) // 2 + i

            curr_profit += ps[j] - ps[mid - 1]
            if j < n -1:
                curr_profit += ss[-1] - ss[j]
            
            if curr_profit > profit:
                profit = curr_profit

            i += 1
            j += 1
        return profit

            
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth_periods = 0
        n = len(prices)
        if n == 1:
            return 1
        
        l , r = 0 , 0
        while r < n:
            if r + 1 < n and prices[r + 1] == prices[r] - 1:
                r += 1
            else:
                l = (r - l + 1)
                smooth_periods += ((l -1) * l) // 2 + l
                l = r + 1
                r += 1
        return smooth_periods


                

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0

        cost = [0] * n
        for i in range(1, n - 1):
            cost[i] = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
        
        res = 0
        if n % 2 != 0:
            for i in range(1, n, 2):
                res += cost[i]
            return res



        @lru_cache(None)
        def rec(i):
            if  i >= n - 1:
                return (0 , 0)

            scnt, sco = rec( i + 1)
            takecnt , takeco = rec( i + 2)
            takecnt += 1
            takeco += cost[i]

            if takecnt > scnt:
                return (takecnt, takeco)
            if takecnt < scnt:
                return (scnt, sco)
            return (takecnt, min(takeco, sco))
        return rec(1)[1]
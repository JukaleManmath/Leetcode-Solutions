class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        n = len(power)
        # memo = {}

        # def dfs(i , prev):
        #     if i >= n:
        #         return 0
        #     key = (i, prev)
        #     if key in memo:
        #         return memo[key]
            
        #     res = dfs(i+1, prev)

        #     if power[i] > prev + 2 or power[i] < prev - 2 or power[i] == prev:
        #         res =  max(res , power[i] + dfs(i + 1,  power[i]))
        #     memo[key] = res
        #     return res
        
        # return dfs(0, float("-inf"))

        val , earn = [] , []
        i = 0
        while i < n:
            v = power[i]
            total = 0
            while  i < n and power[i] == v:
                total += v
                i+=1
            val.append(v)
            earn.append(total)
        
        m = len(val)
        dp = [0] * (m + 1)
        for i in range(m -1, -1, -1):
            next_idx = bisect_left(val, val[i] + 3)
            take = earn[i] + dp[next_idx]
            skip = dp[i+1]
            dp[i] = max(take, skip)
        return dp[0]

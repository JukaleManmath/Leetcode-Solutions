class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        def rec(ind, t):
            if ind == 0:
                if t == 0 or t % coins[0] == 0:
                    return 1
                return 0
            if dp[ind][t] != -1:
                return dp[ind][t]
            nopick = rec(ind - 1, t)
            pick = 0
            if coins[ind] <= t:
                pick = rec(ind, t - coins[ind])
            
            dp[ind][t] =  pick + nopick
            return dp[ind][t]

        return rec(n-1, amount)
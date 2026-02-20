class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        def rec(ind, t):
            if t == 0:
                return 0
            if ind == 0:
                return t//coins[0] if t % coins[0] == 0 else float("inf")
            if dp[ind][t] != -1:
                return dp[ind][t]
            
            notake = rec(ind - 1, t)
            take = float("inf")
            if t >= coins[ind]:
                take = 1 + rec(ind , t - coins[ind])
            
            dp[ind][t] =  min(notake, take)
            return dp[ind][t]
        ans =  rec(n - 1, amount) 
        return ans if ans != float("inf") else -1
            
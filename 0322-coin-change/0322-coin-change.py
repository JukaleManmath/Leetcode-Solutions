class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}
        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     if amount in memo:
        #         return memo[amount]
        #     res = float("inf")
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount- coin))
        #     memo[amount] = res
        #     return res
        # mincoins = dfs(amount)
        # return -1 if mincoins == float("inf") else mincoins

        #  Bottom- up approach
        inf = float("inf")
        dp  = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != inf else -1
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = 1e5

        for i in range(1, n):
            for j in range(0, amount + 1):
                notake = dp[i-1][j]
                take = float("inf")
                if coins[i] <= j:
                    take = 1 + dp[i][j - coins[i]]
                dp[i][j] = min(take, notake)
        
        return dp[n-1][amount] if dp[n-1][amount] != 1e5 else -1
        
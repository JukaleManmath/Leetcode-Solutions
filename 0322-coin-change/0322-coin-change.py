class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        n = len(coins)
        dp = [[float("inf") for _ in range(amount + 1)] for _ in range(n)] 
        def dfs(i, tar):
            if i >= n:
                if tar == 0:
                    return 0
                else:
                    return float("inf")
            if dp[i][tar] != float("inf"):
                return dp[i][tar]
            if tar == 0:
                return 0
            take = float("inf")
            if coins[i] <= tar:
                take = dfs(i + 1 , tar % coins[i]) + (tar // coins[i])
            notake = dfs(i  + 1, tar)

            dp[i][tar] =  min(take, notake)
            return dp[i][tar]
        res  = dfs(0 , amount)
        return res if res != float("inf") else -1


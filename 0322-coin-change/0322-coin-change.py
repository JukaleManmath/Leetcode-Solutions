class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)] 
        # def rec(i, tar):
        #     if tar == 0:
        #         return 0
        #     if i == 0:
        #         return tar // coins[0] if tar % coins[0] == 0 else float("inf")

        #     if dp[i][tar] != -1:
        #         return dp[i][tar]
            
        #     notake = rec(i - 1, tar)
        #     take= float("inf")
        #     if tar >=  coins[i]:
        #         take = 1 + rec(i, tar - coins[i])
        #     dp[i][tar] = min(take, notake)
        #     return dp[i][tar]
        
        # res = rec(n-1, amount)
        # if res == float("inf"):
        #     return -1
        # return res
        
        # tabulation
        
        prev , curr = [0] * (amount + 1), [0] * (amount + 1)

        for t in range(amount + 1):
            if t % coins[0] == 0:
                prev[t] = t // coins[0]
            else:
                prev[t] = float("inf")
        
        for i in range(1, n):
            for t in range(amount + 1):
                notake = prev[t]
                take = float("inf")
                if coins[i] <= t:
                    take = 1 + curr[t - coins[i]]
                curr[t] = min(take, notake)
            prev = curr
        
        return prev[amount] if prev[amount] != float("inf") else -1


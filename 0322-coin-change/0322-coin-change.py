class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        prev , curr = [0] * (amount + 1), [0] *(amount + 1)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]
            else:
                prev[i] = float("inf")
        
        for i in range(1,n):
            for j in range(amount + 1):
                notake = prev[j]
                take = float("inf")
                if coins[i] <= j:
                    take = 1 + curr[j - coins[i]]
                curr[j] = min(take, notake)
            prev = curr
        
        ans = prev[amount]
        if ans == float("inf"):
            return -1
        return ans
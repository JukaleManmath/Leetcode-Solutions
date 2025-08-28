class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # state : choose if possible or move on
        dp = {}  # key (i,amount)
        coins.sort()
        def dfs(i, amount):
            if amount == 0 :
                return 1
            if i >= len(coins):
                return 0
            if (i,amount) in dp:
                return dp[(i,amount)]
            res = 0
            if coins[i] <= amount:
                res = dfs(i+1, amount)
                res += dfs(i, amount - coins[i])
            dp[(i,amount)] = res
            return dp[(i,amount)]
                
        return dfs(0, amount)
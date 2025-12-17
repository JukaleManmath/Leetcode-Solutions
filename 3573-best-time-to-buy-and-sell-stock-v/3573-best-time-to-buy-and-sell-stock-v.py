class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # cache = {}
        # def dfs(i, prev, typet, istransaction, rk):
        #     if i == n:
        #         return 0
        #     if rk <= 0:
        #         return 0
        #     if (i, prev, typet, istransaction, rk) in cache:
        #         return cache[(i, prev, typet, istransaction, rk)]
        #     ans = 0
        #     if prev and prev <= prices[i] and istransaction and typet == "buy":
        #         ans = max(ans , dfs(i + 1, 0, "no", False, rk - 1) + prices[i] - prev, dfs(i + 1, prev, typet, istransaction, rk))
        #     elif not prev and not istransaction and typet == "no":
        #         ans = max(ans , dfs(i + 1, prices[i], "buy", True, rk))
        #         ans = max(ans, dfs(i + 1, prices[i], "sell", True, rk))
        #         ans = max(ans, dfs(i + 1, prev, typet, istransaction, rk))
        #     elif prev and prev >= prices[i] and istransaction and typet == "sell":
        #         ans = max(ans, dfs(i + 1, 0, "no", False, rk - 1) + prev - prices[i], dfs(i + 1, prev, typet, istransaction, rk))
            
        #     cache[(i, prev, typet, istransaction, rk)] = ans
        #     return ans
        # return dfs(0,0,"no", False, k)

        # recursive function with 3 states
        # i -> current day, t-> completed transaction, , state -> 0 (no position) , 1 (holding a long position), 2(holding a short postion)

        # at each day:
        # we can always choose to skip the day
        # if we are not holding any positio, we can open a long or short postion
        # if we are holding a long position, we can sell it to complete a transaction
        # if we are holding a short position, we can buy it back to complete a trasaction


        # memoization ensures each step is computed only once
        # complexity -> O(n*k* 3)
        neg = -10 **18
        dp = [[[None] * 3 for _ in range(k + 1)]for _ in range(n + 1)]

        def dfs(i, t, state):
            if i == n:
                return 0 if state == 0 else neg
            if dp[i][t][state] is not None:
                return dp[i][t][state]
            
            ans = dfs(i + 1, t, state)

            if state == 0:
                ans = max(ans, dfs(i + 1, t , 1) - prices[i])
                ans = max(ans, dfs(i + 1, t, 2) + prices[i])
            elif state == 1 and t < k:
                ans = max(ans, dfs(i + 1, t + 1, 0) + prices[i])
            elif state == 2 and t < k:
                ans = max(ans, dfs(i + 1, t + 1, 0) -prices[i])
            dp[i][t][state] = ans
            return ans
        return dfs(0,0,0)

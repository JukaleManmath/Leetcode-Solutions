class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        memo = {}
        def dfs(i , l):
            if l % 2 != 0:
                ones = s[i:i + l].count("1")
                cost = flatCost if ones == 0 else ones * encCost * l
                return cost
            if (i, l) in memo:
                return memo[(i,l)]
            half = l // 2
            left = dfs(i, half)
            right = dfs(i + half, half)
            
            currones = s[i: i + l].count("1")
            res = flatCost if currones == 0 else currones * encCost * l

            res = min(res, left + right)
            memo[(i,l)] = res
            return res
        return dfs(0, len(s))


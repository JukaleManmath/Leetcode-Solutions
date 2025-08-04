class Solution:
    def climbStairs(self, n: int) -> int:
        steps= [-1] * (n+1)
        def dfs(i):
            if i == 0 or i == 1:
                return 1
            if steps[i] != -1:
                return steps[i]
            steps[i] = dfs(i - 1) + dfs(i-2)
            return steps[i]
        return dfs(n)
        
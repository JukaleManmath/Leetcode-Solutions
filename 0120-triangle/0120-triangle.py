class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float("inf") for _ in range(i + 1)] for i in range(n)]
        def rec(i, j):
            if dp[i][j] != float("inf"):
                return dp[i][j]
            
            if i == n-1:
                return triangle[i][j]
            down = triangle[i][j] + rec(i + 1, j)
            diag = triangle[i][j] + rec(i + 1, j + 1)
            dp[i][j] = min(down, diag)
            return dp[i][j]
        return rec(0, 0)

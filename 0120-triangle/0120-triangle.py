class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float("inf") for _ in range(i + 1)] for i in range(n)]
    
        for i in range(n-1, -1, -1):
            for j in range(i + 1):
                if i == n -1:
                   dp[i][j] = triangle[i][j]
                   continue
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j] , dp[i + 1][j + 1])

        return dp[0][0]

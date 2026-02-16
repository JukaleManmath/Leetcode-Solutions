class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]

            
            
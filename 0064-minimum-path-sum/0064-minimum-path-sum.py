class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def rec(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            up , left = float("inf") , float("inf")
            if i > 0:
                up = rec(i-1, j)
            if j > 0:
                left = rec(i, j -1)
            
            dp[i][j] =  grid[i][j] + min(up, left)
            return dp[i][j]
        return rec(m-1, n-1)
            
            
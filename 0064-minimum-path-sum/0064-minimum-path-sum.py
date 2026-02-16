class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        prev = [0] * n

        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                    continue
                up , left = float("inf"), float("inf")
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = curr[j-1]
                curr[j] = grid[i][j] + min(up, left)
            prev = curr
        
        return curr[n-1]

            
            
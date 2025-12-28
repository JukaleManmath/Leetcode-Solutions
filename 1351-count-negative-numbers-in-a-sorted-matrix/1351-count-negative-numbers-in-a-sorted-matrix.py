class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        m , n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    cnt += 1
        return cnt
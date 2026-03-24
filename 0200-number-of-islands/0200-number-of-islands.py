class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n  = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]

        dir = [[1, 0], [-1, 0], [0,1], [0,-1]]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == "0" or seen[i][j]:
                return
            
            seen[i][j] = True
            for x, y in dir:
                nx, ny = i + x, j + y
                dfs(nx, ny)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not seen[i][j]:
                    res += 1
                    dfs(i, j)
        return res
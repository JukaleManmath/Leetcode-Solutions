class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        dp = {}
        m , n = len(grid), len(grid[0])
        def dfs(i, j , rem):
            if not 0 <= i < m or not 0<= j < n:
                return 0
            
            if (i, j , rem) in dp:
                return dp[(i, j, rem)]
            
            if i == m-1 and j == n -1 and (grid[i][j] + rem) % k == 0:
                return 1
            
            res = dfs(i + 1, j , (grid[i][j] + rem) % k) + dfs(i , j + 1 , (grid[i][j] + rem) % k)
            dp[(i,j,rem)] = res % mod
            return res % mod
        return dfs(0,0,0)

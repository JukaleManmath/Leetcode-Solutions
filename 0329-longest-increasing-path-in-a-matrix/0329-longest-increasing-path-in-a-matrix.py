class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        cnt = 0
        m , n = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, p):
            if min(i, j) < 0 or i >= m or j >= n or matrix[i][j] <= p:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for di, dj in direction:
                ni = i + di
                nj = j + dj
                res = max(res ,1 + dfs(ni, nj, matrix[i][j]))
            dp[(i,j)] = res
            return res
        
        LIP = 0
        for i in range(m):
            for j in range(n):
                LIP = max(LIP , dfs(i, j , float(-inf)))
        return LIP
    
            
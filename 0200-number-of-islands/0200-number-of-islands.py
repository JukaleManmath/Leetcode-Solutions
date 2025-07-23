class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs 1
        # row , col = len(grid), len(grid[0])
        # visited = [[False]* col for _ in range(row)]
        # count = 0
        
        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0" or visited[r][c]:
        #         return
        #     visited[r][c] = True

        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)

            
        # for r in range(row):
        #     for c in range(col):
        #         if grid[r][c] == "1" and not visited[r][c]:
        #             dfs(r, c )
        #             count += 1
        # return count

        #dfs -2 
        row , col = len(grid), len(grid[0])
        isIlands = 0
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        def dfs(r , c):
            if r < 0 or c <0 or r >= row or c>= col or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    isIlands += 1
        return isIlands
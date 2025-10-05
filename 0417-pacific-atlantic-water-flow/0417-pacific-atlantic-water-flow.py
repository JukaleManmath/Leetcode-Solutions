class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        res = []
        pac , atl = set(), set()
        def dfs(r , c ,visited, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or heights[r][c] < prev:
                return
            visited.add((r,c))
            dfs( r + 1, c , visited, heights[r][c])
            dfs( r - 1, c , visited, heights[r][c])
            dfs( r , c + 1 , visited, heights[r][c])
            dfs( r , c - 1 , visited, heights[r][c])
        
        for i in range(cols):
            dfs(0, i , pac, -1)
            dfs(rows - 1, i , atl , -1)
        
        for j in range(rows):
            dfs(j, 0 , pac, -1)
            dfs(j, cols -1, atl, -1)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i, j) in atl:
                    res.append((i,j))
        
        return res


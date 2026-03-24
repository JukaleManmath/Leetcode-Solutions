class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        res = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in dir:
                    nx, ny = i + x, j + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1

            res += 1
        
        return res if fresh == 0 else -1
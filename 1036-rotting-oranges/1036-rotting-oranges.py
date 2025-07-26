class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        time = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr ,dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc <cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

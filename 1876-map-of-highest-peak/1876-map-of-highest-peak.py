class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n , m = len(isWater), len(isWater[0])
        direction = [[-1,0], [1, 0], [0,1],[0,-1]]
        res = [[0 for _ in range(m)] for _ in range(n) ]
        visited = set()
        q = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append([i, j])
                    visited.add((i,j))
        h = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                res[row][col] = h
                for dr , dc in direction:
                    nr , nc = row + dr , col + dc
                    if (nr,nc) not in visited and 0 <= nr < n and 0 <= nc < m:
                        q.append([nr,nc])
                        visited.add((nr, nc))
            h += 1

        return res

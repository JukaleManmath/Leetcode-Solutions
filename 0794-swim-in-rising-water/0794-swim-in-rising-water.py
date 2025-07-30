class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Djikistras algo
        n = len(grid)
        minheap = [(grid[0][0], 0 , 0)]
        visited = set([(0,0)])
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        while minheap:
            time , i , j = heapq.heappop(minheap)
            if i == n-1 and j == n-1:
                return time
            for di, dj in direction:
                ni, nj = di + i, dj + j
                if ni >= 0 and nj >= 0 and ni <= n-1 and nj <= n-1 and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    heapq.heappush(minheap,(max(time, grid[ni][nj]),ni, nj ))
        return -1
            
            
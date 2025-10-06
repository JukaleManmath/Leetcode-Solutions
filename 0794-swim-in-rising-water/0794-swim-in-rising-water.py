class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1],[0, -1]]
        minheap = [[grid[0][0], 0 , 0]]
        visited = set([(0,0)])
        while minheap:
            time , i , j = heapq.heappop(minheap)
            if i == n-1 and j == n-1:
                return time
            for x , y in directions:
                dx, dy = x + i, y + j
                if 0 <= dx <n and 0 <= dy <n and (dx,dy) not in visited:
                    visited.add((dx,dy))
                    heapq.heappush(minheap, [max(time, grid[dx][dy]), dx, dy])
        return -1


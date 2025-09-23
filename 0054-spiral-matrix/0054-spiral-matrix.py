class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix) 
        cols = len(matrix[0])
        res = []
        x, y, dx, dy = 0 , 0, 0, 1
        for _ in range(rows* cols):
            res.append(matrix[x][y])
            matrix[x][y] = "#"

            if not 0 <= x + dx < rows or not 0 <= y + dy < cols or matrix[x+dx][y+dy] == "#":
                dx ,dy = dy, -dx
            
            x += dx
            y += dy
        
        return res

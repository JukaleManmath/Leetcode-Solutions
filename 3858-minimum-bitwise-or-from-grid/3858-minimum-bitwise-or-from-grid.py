class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        for bit in range(17, -1, -1):
            temp = [[] for _ in range(rows)]
            possible = True
            for i in range(rows):
                for num in grid[i]:
                    if (num & (1 << bit)) == 0:
                        temp[i].append(num)
                    
                if not temp[i]:
                    possible= False
            
            if not possible:
                res = res | (1 << bit)
            else:
                grid = temp
        return res
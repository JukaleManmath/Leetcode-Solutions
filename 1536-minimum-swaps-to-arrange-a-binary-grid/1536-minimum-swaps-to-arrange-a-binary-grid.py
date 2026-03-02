class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []

        for row in range(n):
            count = 0
            for i in range(n-1,-1,-1):
                if grid[row][i] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
        

        swaps = 0
        for i in range(n):
            j = i
            needed = n - i -1
            if zeros[j] >= needed:
                continue
            
            while j < n and zeros[j] < needed:
                j += 1
            if j == n:
                return -1
            
            while j > i:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                swaps += 1
                j -= 1
        return swaps
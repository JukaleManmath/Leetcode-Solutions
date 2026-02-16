class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp = [[float("inf") for _ in range(i + 1)] for i in range(n)]
        nextRow = [0] * n
        curr = [0] * n

        for i in range(n):
            nextRow[i] = triangle[n-1][i]
    
        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                curr[j] = triangle[i][j] + min(nextRow[j] , nextRow[j + 1])
            nextRow = curr
        return nextRow[0]

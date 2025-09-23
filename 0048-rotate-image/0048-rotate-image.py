class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[n-1-i][j] , matrix[i][j] = matrix[i][j],  matrix[n-1-i][j]
        
        i , j = 0 , 0
        for i in range(n):
            for j in range(n):
                if i== j:
                    break
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
            
            
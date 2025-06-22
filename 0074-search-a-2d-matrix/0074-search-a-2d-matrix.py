class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        top , bot = 0 , m
        while (top <= bot):
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot:
            return False
        l ,r = 0 , n
        while l <= r:
            mid = (l + r)// 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
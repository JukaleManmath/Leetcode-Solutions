class Solution:
    def isSafe(self, board, row, col):
        r = row - 1
        c = col
        while r >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
        
        r , c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        r , c = row - 1, col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                solution = ["".join(row) for row in board]
                res.append(solution)
                return
            
            for c in range(n):
                if self.isSafe(board , r, c):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."
        backtrack(0)
        return res
        
        


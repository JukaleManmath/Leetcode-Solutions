class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [[-1,-1], [-1,0],[-1,1], [0, 1],[1,1],[1,0],[1,-1],[0,-1]]
        m , n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                live = 0
                for x , y in direction:
                    if 0 <= i + x <m and 0 <= j + y < n:
                        if board[i+x][j + y] in [1 ,2]:
                            live += 1
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2
                    if live in [2 ,3]:
                        board[i][j] = 1
                elif board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

                
                
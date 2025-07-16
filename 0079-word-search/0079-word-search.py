class Solution:
    def backtrack(self, i, j ,board, word, idx):
        if idx == len(word):
            return True
        
        if (i < 0 or i >= len(board) or j < 0 or 
            len(board[0]) <= j or board[i][j] != word[idx] 
            or board[i][j] == "#"):
            return False

        board[i][j] = "#"
        res = (self.backtrack(i+1,j,board,word,idx+1) or
                 self.backtrack(i-1,j,board,word,idx+1) or 
                 self.backtrack(i,j+1,board,word,idx+1) or 
                 self.backtrack(i,j-1,board,word,idx+1))
        board[i][j] = word[idx]
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.backtrack(i , j , board, word, 0):
                        return True
        return False
                    
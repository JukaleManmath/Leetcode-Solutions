class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                if num in row[r] or num in col[c] or num in box[(r // 3 , c//3)]:
                    return False
                
                row[r].add(num)
                col[c].add(num)
                box[(r//3 , c // 3)].add(num)
        return True

        
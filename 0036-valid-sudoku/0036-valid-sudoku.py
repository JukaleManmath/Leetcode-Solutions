class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        boxes = defaultdict(list)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                if curr in rows[i] or curr in columns[j] or curr in boxes[(i//3,j//3)]:
                    return False
                
                rows[i].append(curr)
                columns[j].append(curr)
                boxes[(i//3,j//3)].append(curr)
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        boxes = defaultdict(list)

        for i in range(9):
            for j in range(9):
                box = (i // 3 , j // 3)
                if board[i][j] == ".":
                    continue
                
                curr = board[i][j]
                if curr in rows[i] or curr in columns[j] or curr in boxes[box]:
                    return False
                columns[j].append(curr)
                rows[i].append(curr)
                boxes[box].append(curr)
        return True
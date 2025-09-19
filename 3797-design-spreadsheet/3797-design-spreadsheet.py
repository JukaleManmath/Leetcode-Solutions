class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet ={}


    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.sheet:
            del self.sheet[cell]

    def getValue(self, formula: str) -> int:
        i = 0
        while i < len(formula):
            if formula[i] == "+":
                left = formula[1:i]
                right = formula[i+1:]

                if left[0].isalpha():
                    valleft = self.sheet.get(left, 0)
                else:
                    valleft = int(left)
                
                if right[0].isalpha():
                    valright = self.sheet.get(right, 0)
                else:
                    valright = int(right)
                return valleft + valright
            i += 1
        




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
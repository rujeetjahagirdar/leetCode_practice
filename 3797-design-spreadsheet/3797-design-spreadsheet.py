class Spreadsheet:

    def __init__(self, rows: int):
        
        self.spreadsheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split("+")

        if(not x.isnumeric()):
            x = self.spreadsheet[x]
        
        if(not y.isnumeric()):
            y = self.spreadsheet[y]

        x, y = int(x), int(y)
        return(x+y)

        return 0

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = [[0] * 26 for _ in range(rows + 1)]
    
    def __parse_cell(self, cell: str):
        row = int(cell[1:])
        col = ord(cell[0]) - ord("A")
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.__parse_cell(cell)
        self.spreadsheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.__parse_cell(cell)
        self.spreadsheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula.replace("=", "").split("+")
        X = Y = None
        if formula[0].isnumeric(): X = int(formula[0])
        else:
            row, col = self.__parse_cell(formula[0])
            X = self.spreadsheet[row][col]
        if formula[1].isnumeric(): Y = int(formula[1])
        else:
            row, col = self.__parse_cell(formula[1])
            Y = self.spreadsheet[row][col]
        return X + Y

class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            raise Exception('Sub rules violation!')
        return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        res = int(self.cell / other.cell)
        if res == 0:
            raise Exception('Div rules violation!')
        return res

    def make_order(self, rows):
        return '\n'.join(map(lambda x: rows * '*', range(self.cell // rows))) + '\n' + self.cell % rows * '*'


cell_1 = Cell(7)
cell_2 = Cell(13)
try:
    print(Cell(cell_1 * cell_2).make_order(14))
    print(10 * "-")
    print(Cell(12).make_order(5))
    print(10 * "-")
    print(Cell(15).make_order(5))
except Exception as e:
    print('Impossible operation: ',  e)

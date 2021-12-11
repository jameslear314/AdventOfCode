INPUT = 'data.11.txt'
TEST0 = 'test.11.0.txt'
RESULT0 = 1656
RESULT1 = 5

class Grid:
    field = []

    def __init__(self, values):
        for row in range(len(values)):
            self.field.append([])
            for column in range(len(values[0])):
                self.field[row].append(column)

        for row in range(len(values)):
            for column in range(len(values[0])):
                self.field[row][column] = Octo(values[row][column], row, column, self)

        for row in range(len(values)):
            for column in range(len(values[0])):
                Octo.link(self.field[row][column], row, column, self)

class Octo:
    value = -1
    row = -1
    column = -1
    neighbors = -1

    def __init__(self, value, row, column, grid):
        self.value = value
        self.row = row
        self.column = column
        self.neighbors = []

    def link(self, row, column, grid):
        rows = [row]
        columns = [column]
        if row > 0:
            rows.append(row - 1)
        if row < len(grid.field) - 1:
            rows.append(row + 1)
        if column > 0:
            columns.append(column - 1)
        if column < len(grid.field[0]) - 1:
            columns.append(column + 1)

        for r in rows:
            for c in columns:
                if r != row or c != column:
                    self.neighbors.append(grid.field[r][c])

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    values = prep(cases)
    grid = Grid(values)

    # print(len(grid.field[2][3].neighbors))
    # neighbors = grid.field[0][0].neighbors
    # for n in neighbors:
    #     print(n.value)

def solve2(cases):
    grid = prep(cases)
    return None

def prep(cases):
    grid = []
    for case in cases:
        row = []
        for char in case:
            row.append(int(char))
        grid.append(row)
    return grid

if __name__ == '__main__':
    data = loadData(INPUT)
    test = loadData(TEST0)

    print(test)

    test_results = solve(test)
    if test_results != RESULT0:
        print(test_results, 'should be {}'.format(RESULT0))
        exit()
    print('results', test_results)

    results = solve(data)
    print(results)

    test_results = solve2(test)

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve2(data)
    print(results)
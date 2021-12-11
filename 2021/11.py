INPUT = 'data.11.txt'
TEST0 = 'test.11.0.txt'
RESULT0 = 1656
RESULT1 = 5

class Grid:
    field = []
    flashed = []
    rows = -1
    columns = -1

    def __init__(self, values):
        rowlength = len(values)
        self.rows = rowlength
        columnlength = len(values[0])
        self.columns = columnlength
        for row in range(rowlength):
            self.field.append([])
            self.flashed.append([])
            for column in range(columnlength):
                self.field[row].append(column)
                self.flashed[row].append(False)

        for row in range(rowlength):
            for column in range(columnlength):
                self.field[row][column] = Octo(values[row][column], row, column, self)

        for row in range(rowlength):
            for column in range(columnlength):
                Octo.link(self.field[row][column], row, column, self)
        print(self.rows, self.columns)

    def propagate(self, step=0):
        flashcount = 0
        # Add 1 to all octos; reset the flashing
        for row in range(self.rows):
            for column in range(self.columns):
                octo = self.field[row][column]
                octo.value += 1
                octo.flashed = False

        proceed = True
        while proceed: # Flash all octopuses until they are done
            flashstep = False
            for row in range(self.rows):
                for column in range(self.columns):
                    if self.field[row][column].flash():
                        flashstep = True
                        flashcount += 1
            if not flashstep: # When no more octopuses flash, break the loop
                proceed = False

        return flashcount

    def __repr__(self) -> str:
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.field[row][column].value, end = '')
            print()

class Octo:
    value, row, column, neighbors, grid = None, None, None, None, None

    def __init__(self, value, row, column, grid):
        self.value = value
        self.row = row
        self.column = column
        self.neighbors = []
        self.grid = grid

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

    def flash(self):
        flashed = False
        if not self.grid.flashed[self.row][self.column] and self.value > 9:
            flashed = True
            for neighbor in self.neighbors:
                neighbor.value += 1
            self.grid.flashed[self.row][self.column] = True
        return flashed

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    values = prep(cases)
    grid = Grid(values)

    total = 0
    for i in range(10):
        total += grid.propagate(i)
        print(i, total)
        grid.__repr__()

    return total

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
INPUT = 'data.11.txt'
TEST0 = 'test.11.0.txt'
RESULT0 = 1656
RESULT1 = 195

tests = {
0: '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526''',
1: '''6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637''',
2:'''8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848''',
3:'''0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000''',
4:'''2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211''',
5:'''4484144000
2044144000
2253333493
1152333274
1187303285
1164633233
1153472231
6643352233
2643358322
2243341322''',
6:'''5595255111
3155255222
3364444605
2263444496
2298414396
2275744344
2264583342
7754463344
3754469433
3354452433''',
7:'''6707366222
4377366333
4475555827
3496655709
3500625609
3509955566
3486694453
8865585555
4865580644
4465574644''',
8:'''7818477333
5488477444
5697666949
4608766830
4734946730
4740097688
6900007564
0000009666
8000004755
6800007755''',
9:'''9060000644
7800000976
6900000080
5840000082
5858000093
6962400000
8021250009
2221130009
9111128097
7911119976''',
10:'''0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000''',
}

class Grid:
    field, flashed, rows, columns = None, None, None, None

    def __init__(self, values):
        self.field = []
        self.flashed = []
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
        if len(self.field) != rowlength:
            print("Incorrect number of rows. Have", len(self.field), 'instead of', rowlength)
            exit()
        for i in range(rowlength):
            if len(self.field[i]) != columnlength:
                print("Incorrect number of columns. Have", len(self.field[i]), 'instead of', columnlength)
                exit()

        added = 0
        for row in range(rowlength):
            for column in range(columnlength):
                added += 1
                self.field[row][column] = Octo(values[row][column], row, column, self)
        if added != rowlength * columnlength:
            print("Failed to add the right octos", added)
            exit()

        for row in range(rowlength):
            for column in range(columnlength):
                print(row, rowlength, column, columnlength)
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

    def reset(self):
        for row in range(self.rows):
            for column in range(self.columns):
                octo = self.field[row][column]
                if octo.value > 9:
                    octo.value = 0
                self.flashed[row][column] = False

    def __repr__(self) -> str:
        output = []
        for row in range(self.rows):
            line = []
            for column in range(self.columns):
                line.append(str(self.field[row][column].value))
            output.append(''.join(line))
        return '\n'.join(output)

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
                    row = grid.field[r]
                    octo = row[c]
                    self.neighbors.append(octo)

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

def printFlashes(grid):
    for i in range(10):
        for j in range(10):
            print(grid.flashed[i][j], end='')
        print()

def solve(cases, testing=False):
    values = prep(cases)
    grid = Grid(values)

    total = 0
    for i in range(100):
        if i in tests:
            if testing and str(grid) != tests[i]:
                print("FAILED: Grid was")
                print(str(grid))
                print("and should have been")
                print(tests[i])
                print("after step", i)
                exit()
        total += grid.propagate(i)
        # print(i, total)
        grid.reset()
        # print(grid)

    return total

    # print(len(grid.field[2][3].neighbors))
    # neighbors = grid.field[0][0].neighbors
    # for n in neighbors:
    #     print(n.value)

def solve2(cases):
    values = prep(cases)
    grid = Grid(values)

    i = 1
    while True:
        grid.propagate(i)
        allFlash = True
        for r in range(grid.rows):
            for c in range(grid.columns):
                if not grid.flashed[r][c]:
                    allFlash = False
                    break
        grid.reset()
        if allFlash:
            return i
        i += 1

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

    test_results = solve(test, True)
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
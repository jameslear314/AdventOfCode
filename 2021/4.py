INPUT = 'data.4.txt'
TEST0 = 'test.4.0.txt'
RESULT0 = 4512
RESULTSUM = 199
RESULTNUM = 24
RESULT1 = 5

class Board:
    values = []
    boardRowLimit = 5
    boardColLimit = 5
    def __init__(self, lines):
        if len(lines) != self.boardRowLimit + 1: # Empty first line
            print("ERROR: Board was of wrong shape:", len(lines), len(lines[-1]))
            print("Should be", self.boardRowLimit, "x", self.boardColLimit)
            exit()
            
        for line in lines:
            if len(line) and line: #First line is empty
                vals = line.split(' ') #space separated
                vals = [int(v) for v in vals if v]
                for val in vals:
                    self.values.append(Value(val)) # Store value and if it has been hit
    
    def completedRow(self, rowIndex):
        minValToCheck = rowIndex * self.boardColLimit
        maxValToCheck = minValToCheck + self.boardColLimit
        valToCheck = minValToCheck
        while valToCheck < maxValToCheck:
            if not self.values[valToCheck].hit:
                return False
        return True

    def completedColumn(self, columnIndex):
        for i in range(columnIndex, len(self.values), self.boardColLimit):
            if not self.values[i].hit:
                return False
        return True

    def completed(self):
        for r in range(self.boardRowLimit):
            if self.completedRow(r):
                return True
        for c in range(self.boardColLimit):
            if self.completedColumn(c):
                return True
        return False




class Value:
    number = -1
    hit = False
    def __init__(self, number):
        self.number = number

    def call(self):
        self.hit = True



def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    val = cases[0]
    result = 0
    for case in cases[1:]:
        if case > val:
            result += 1
        val = case
    return result

def solve2(cases):
    return None

def prep(data):
    drawlist = data[0]
    data = data[1:]

    draws = drawlist.split(',')
    
    # Data is now a structured set of lines
    # One blank, followed by 5 lines of 5 numbers
    # Separated by spaces.
    boards = []
    while len(data) >= 6: # Magic number
        boards.append(Board(data[:6]))
        data = data[6:]
    
    return ([int(d) for d in draws], boards)


if __name__ == '__main__':
    datad = loadData(INPUT)
    testd = loadData(TEST0)

    data = prep(datad)
    test = prep(testd)

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
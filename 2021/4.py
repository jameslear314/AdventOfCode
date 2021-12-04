INPUT = 'data.4.txt'
TEST0 = 'test.4.0.txt'
RESULT0 = 4512
RESULTSUM = 199
RESULTNUM = 24
RESULT1 = 1924

class Board:
    values = []
    boardRowLimit = 5
    boardColLimit = 5
    completeAt = None
    def __init__(self, lines):
        self.values = []
        if len(lines) != self.boardRowLimit + 1: # Empty first line
            print("ERROR: Board was of wrong shape:", len(lines), len(lines[-1]))
            print("Should be", self.boardRowLimit, "x", self.boardColLimit)
            exit()

        for line in lines:
            if len(line) and line: #First line is empty
                vals = line.split(' ') #space separated
                vals = [int(v) for v in vals if v]
                for val in vals:
                    storedValue = Value(val)
                    self.values.append(storedValue) # Store value and if it has been hit
    
    def completedRow(self, rowIndex):
        minValToCheck = rowIndex * self.boardColLimit
        maxValToCheck = minValToCheck + self.boardColLimit
        valToCheck = minValToCheck
        while valToCheck < maxValToCheck:
            if not self.values[valToCheck].hit:
                return False
            valToCheck += 1 # Sigh, of course I didn't terminate the loop
        return True

    def completedColumn(self, columnIndex):
        for i in range(columnIndex, len(self.values), self.boardColLimit):
            if not self.values[i].hit:
                return False
        return True

    def completed(self, callNumber = -1):
        for r in range(self.boardRowLimit):
            if self.completedRow(r):
                if not self.completeAt:
                    self.completeAt = callNumber
                return True
        for c in range(self.boardColLimit):
            if self.completedColumn(c):
                if not self.completeAt:
                    self.completeAt = callNumber
                return True
        return False

    def draw(self, value):
        for v in self.values:
            if v.number == value:
                v.call()
                return
        return

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
    draws = cases[0]
    boards = cases[1]
    winboard = None
    wincall = -1

    for board in boards:
        outputVals(board)
        print()
    
    count = 0
    for draw in draws:
        print("Draw:", draw)
        count += 1
        for i in range(len(boards)):
            board = boards[i]
            board.draw(draw)
            if board.completed():
                winboard = board
                wincall = draw
                print("Found winning board", board, wincall)
            if winboard:
                break
        
        # if count in [5, 11] or draw in [24]: #Count check should be 
        #     print("Output at", count)
        #     for board in boards:
        #         output(board)
        #         print()
        if winboard:
            break
    
    return score(winboard, wincall)


def solve2(cases):
    draws = cases[0]
    boards = cases[1]
    winboard = None
    wincall = -1
    wonboards = []

    for board in boards:
        outputVals(board)
        print()
    
    count = 0
    for draw in draws:
        print("Draw:", draw)
        count += 1
        boardLen = len(boards)
        boardsToDel = []
        for i in range(len(boards)):
            board = boards[i]
            board.draw(draw)
            if board.completed(i):
                wonboards.append(board)
                wincall = draw
                print("Found winning board", board, wincall)
                boardsToDel.append(i)
        boardsToDel.sort(reverse=True)
        for delable in boardsToDel:
            del(boards[delable])
        
    
    return score(wonboards[-1], wincall)

def score(board, lastCall):
    unmarked = [v.number for v in board.values if not v.hit]
    unmarkSum = sum(unmarked)
    return unmarkSum * lastCall

def outputVals(board):
    for i in range(board.boardRowLimit):
        for j in range(board.boardColLimit):
            val = board.values[i * board.boardColLimit + j].number
            valLen = len(str(val))
            terminator = ' ' * (3 - valLen)
            print(val, end=terminator)
        print()

def output(board):
    hits = []
    for i in range(board.boardRowLimit):
        for j in range(board.boardColLimit):
            if board.values[i * board.boardColLimit + j].hit:
                print('x', end=' ')
            else:
                print('.', end=' ')
        print()

def prep(data):
    drawlist = data[0]
    data = data[1:]

    draws = drawlist.split(',')
    
    # Data is now a structured set of lines
    # One blank, followed by 5 lines of 5 numbers
    # Separated by spaces.
    boards = []
    boardSize = 5
    for i in range(0, len(data), boardSize + 1):
        board = Board(data[i:i+boardSize + 1])
        boards.append(board)

    print(len(data), len(boards))
    return ([int(d) for d in draws], boards)


if __name__ == '__main__':
    datad = loadData(INPUT)
    testd = loadData(TEST0)

    test = prep(testd)
    test_results = solve(test)
    if test_results != RESULT0:
        print(test_results, 'should be {}'.format(RESULT0))
        exit()
    print('results', test_results)

    data = prep(datad)
    results = solve(data)
    print(results)

    test_results = solve2(test)

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve2(data)
    print(results)
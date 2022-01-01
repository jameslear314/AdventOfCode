INPUT = 'data.15.txt'
TEST0 = 'test.15.0.txt'
RESULT0 = 40
RESULT1 = 315
import math

MAXSCORE = 1000 * 1000 * 1000 * 1000 # /shrug # This puzzle probably doesn't reach a score of 1 Trillion

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

class Record:
    score, x, y = None, None, None
    xlow, xhigh = None, None
    ylow, yhigh = None, None

    def __init__(self, x, y, grid, last=None) -> None:
        self.x, self.y = x, y
        if last is not None:
            self.score = last.score + grid[x][y]
        else:
            self.score = 0
        if x != 0:
            self.xlow = True
        if y != 0:
            self.ylow = True
        if x < len(grid) - 1:
            self.xhigh = True
        if y < len(grid[x]) - 1:
            self.yhigh = True

    def __repr__(self) -> str:
        return ''.join([str(self.x), ',', str(self.y), ': ', str(self.score)])

def solve(cases):
    grid, scores, visited = prep(cases)
    endx, endy = len(grid), len(grid[0])
    scoreReached = 0

    records = {}
    x = 0
    y = 0
    start = Record(x, y, grid)
    scores[x][y] = start.score
    records[(x, y)] = start
    visited[x][y] = True
    currents = {}
    for item in Record(1, 0, grid, start), Record(0, 1, grid, start):
        score = item.score
        x, y = item.x, item.y
        if x == endx and y == endy: # When it stumbles on the end, stop travelling
            return item.score
        if visited[x][y]:
            continue
        if score not in currents:
            currents[score] = []
        currents[score].append(item)

    loop = 0
    while len(currents) > 0: # If the item is the end, it bails
        loop += 1
        nexts = {}
        keys = list(currents.keys())
        keys.sort()
        for key in keys:
            points = currents[key]
            items = set()
            for point in points:
                x, y = point.x, point.y
                if x == endx - 1 and y == endy - 1:
                    return point.score

                visit = visited[x][y]
                if visit:
                    continue
                visited[x][y] = True

                # Consider the adjacent points
                potentials = []
                if point.xlow:
                    potentials.append(Record(x - 1, y, grid, point))
                if point.ylow:
                    potentials.append(Record(x, y - 1, grid, point))
                if point.xhigh: 
                    potentials.append(Record(x + 1, y, grid, point))
                if point.yhigh:
                    potentials.append(Record(x, y + 1, grid, point))
                for potential in potentials:
                    if not visited[potential.x][potential.y]:
                        score = potential.score
                        if score not in nexts:
                            nexts[score] = []
                        nexts[score].append(potential)

        currents = nexts


def solve2(cases):
    grid, scores, visited = prep(cases)
    grid, scores, visited = expand(grid, scores, visited)
    endx, endy = len(grid), len(grid[0])
    scoreReached = 0

    records = {}
    x = 0
    y = 0
    start = Record(x, y, grid)
    scores[x][y] = start.score
    records[(x, y)] = start
    visited[x][y] = True
    currents = {}
    for item in Record(1, 0, grid, start), Record(0, 1, grid, start):
        score = item.score
        x, y = item.x, item.y
        if x == endx and y == endy: # When it stumbles on the end, stop travelling
            return item.score
        if visited[x][y]:
            continue
        if score not in currents:
            currents[score] = []
        currents[score].append(item)

    loop = 0
    while len(currents) > 0: # If the item is the end, it bails
        loop += 1
        nexts = {}
        keys = list(currents.keys())
        keys.sort()
        for key in keys:
            points = currents[key]
            items = set()
            for point in points:
                x, y = point.x, point.y
                if x == endx - 1 and y == endy - 1:
                    return point.score

                visit = visited[x][y]
                if visit:
                    continue
                visited[x][y] = True

                # Consider the adjacent points
                potentials = []
                if point.xlow:
                    potentials.append(Record(x - 1, y, grid, point))
                if point.ylow:
                    potentials.append(Record(x, y - 1, grid, point))
                if point.xhigh: 
                    potentials.append(Record(x + 1, y, grid, point))
                if point.yhigh:
                    potentials.append(Record(x, y + 1, grid, point))
                for potential in potentials:
                    if not visited[potential.x][potential.y]:
                        score = potential.score
                        if score not in nexts:
                            nexts[score] = []
                        nexts[score].append(potential)

        currents = nexts


def expand(grid, scores, visited, multiplier=5):
    nextgrid, nextscores, nextvisited = {}, {}, {}
    # The grid becomes tiled, in which each copy to the right or below adds 1 to each score
    # Each score is mod 9 of the score, I think.
    xlen = len(grid) * 5
    ylen = len(grid[0]) * 5


def prep(cases):
    grid, scores, visited = {}, {}, {}
    for i in range(len(cases)):
        row, scorerow, visitedrow = {}, {}, {}
        for j in range(len(cases[i])):
            row[j] = int(cases[i][j])
            scorerow[j] = MAXSCORE
            visitedrow[j] = False
        grid[i] = row
        scores[i] = scorerow
        visited[i] = visitedrow

    return grid, scores, visited

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
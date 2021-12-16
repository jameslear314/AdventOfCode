INPUT = 'data.15.txt'
TEST0 = 'test.15.0.txt'
RESULT0 = 40
RESULT1 = 5
import math

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

class Position:
    x = -1
    y = -1
    grid = None

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid
    
    def dtogoal(self):
        xd = self.grid.x - self.x
        yd = self.grid.y - self.y
        return math.sqrt(xd * xd + yd * yd)
    
    def __repr__(self) -> str:
        return "{},{}".format(self.x, self.y)

class Path:
    endscore = None
    positions = None
    candidates = None
    used = None
    grid = None
    direction = None

    def __init__(self, next, grid, forepath=None, direction=True):
        self.positions = []
        self.used = set()
        self.grid = grid
        if forepath is not None:
            direction = forepath.direction
        else:
            self.direction = direction
        if forepath is not None:
            self.positions = forepath.positions[:]
        if next:
            self.positions.append(next)
        else:
            self.positions.append(Position(0, 0, grid))

        for position in self.positions:
            self.used.add((position.x, position.y))

        score = 0
        for position in self.positions:
            if position.x != 0 or position.y != 0:
                score += grid.field[position.x][position.y]
        self.endscore = score

        self.candidates = []
        xs = []
        ys = []
        if position.x > 0:
            xs.append(position.x - 1)
        if position.y > 0:
            ys.append(position.y - 1)
        if position.x < grid.x - 1:
            xs.append(position.x + 1)
        if position.y < grid.y - 1:
            ys.append(position.y + 1)
        for x in xs:
            candidate = Position(x, position.y, grid)
            self.candidates.append(candidate)
        for y in ys:
            candidate = Position(position.x, y, grid)
            self.candidates.append(candidate)

    def complete(self):
        end = self.positions[-1]
        coord = (end.x, end.y)
        if self.direction:
            return end.x == self.grid.x - 1 and end.y == self.grid.y - 1, self.endscore
        else:
            if coord in self.grid.used and self.grid.used[coord].direction:
                return True, self.endscore + self.grid.used[(end.x, end.y)]
        return False, self.endscore

    def __repr__(self) -> str:
        return "{}: {}".format(self.endscore, self.positions[-1].dtogoal())

class ScoreGrid:
    field = None
    grid = None
    positive = None
    negative = None

    def __init__(self, grid):
        self.field = []
        self.grid = grid
        for x in range(grid.x):
            row = []
            for y in range(grid.y):
                row.append(None)
            self.field.append(row)

    def register(self, path):
        end = path.positions[-1]
        score = path.endscore
        direction = 1 if path.direction else -1

        dirscore = direction * score

        existingscore = self.field[end.x][end.y]
        registered = False
        if existingscore is None:
            self.field[end.x][end.y] = dirscore
            registered = True
        
        elif direction == 1:
            if existingscore > dirscore:
                self.field[end.x][end.y] = dirscore
                registered = True
        else:
            if existingscore < dirscore:
                self.field[end.x][end.y] = dirscore
                registered = True

        if not registered:
            return [] # Don't continue processing candidates if a cheaper path was here first

        # This score is the cheapest known score.
        # Send out candidates which are cheaper than their next spots
        goodCandidates = []
        for candidate in path.candidates:
            x = candidate.x
            y = candidate.y
            nextscore = self.grid[x][y]
            maybescore = dirscore + direction * nextscore

class Grid:
    field = None
    x = None
    y = None
    used = None
    def __init__(self, field):
        self.field = field
        self.x = len(field)
        self.y = len(field[0])
        self.used = {}
    
    def __repr__(self) -> str:
        return str(self.field)

def solve(cases):
    grid = prep(cases)

    endPath = Path(None, grid)
    endScore = grid.field[grid.x - 1][grid.y - 1]
    endPath.endscore = endScore
    endPath.direction = False
    endpoint = Position(grid.x - 1, grid.y - 1, grid)
    endPath.positions = [endpoint]
    endPath.used.add(endpoint)
    endPath.candidates = [Position(grid.x - 2, grid.y - 1, grid), Position(grid.x - 1, grid.y - 2, grid)]
    trips = {0:[Path(None, grid, forepath=None, direction=True)], endScore:[endPath]}
    finished = False
    while not finished:
        nextkey = min(trips.keys())
        print(nextkey)
        
        currents = trips[nextkey]
        for current in currents:
            if current.complete()[0]:
                return current.complete()
            
            for candidate in current.candidates:
                coords = (candidate.x, candidate.y)
                if coords in current.used:
                    continue
                nextPath = Path(candidate, grid, current)
                score = nextPath.endscore
                if score not in trips:
                    trips[score] = [nextPath]
                else:
                    trips[score].append(nextPath)
                if coords not in grid.used:
                    grid.used[coords] = nextPath
        
        del(trips[nextkey])


def solve2(cases):
    return None


def prep(cases):
    grid = []
    for case in cases:
        row = []
        for char in case:
            row.append(int(char))
        grid.append(row)
    return Grid(grid)

if __name__ == '__main__':
    data = loadData(INPUT)
    test = loadData(TEST0)

    print(test)

    grid = prep(test)
    start = Path(Position(0, 0, grid), grid)
    next = Path(Position(1, 0, grid), grid)

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
INPUT = 'data.5.txt'
TEST0 = 'test.5.0.txt'
RESULT0 = 5
RESULT1 = 12

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

class Dot:
    x = -1
    y = -1

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    points = None

    def __init__(self, p1, p2):
        self.points = (p1,p2)

def solve(cases):
    vents = {}
    for line in cases:
        start = line.points[0]
        end = line.points[1]
        if start.x != end.x and start.y != end.y:
            continue
        if start.x == end.x:
            x = start.x
            ends = start.y, end.y
            for i in range(min(ends), max(ends) + 1):
                if (x,i) not in vents:
                    vents[(x,i)] = 1
                else:
                    vents[(x,i)] += 1
        elif start.y == end.y:
            y = start.y
            ends = start.x, end.x
            for i in range(min(ends), max(ends) + 1):
                if (i,y) not in vents:
                    vents[(i,y)] = 1
                else:
                    vents[(i,y)] += 1
    
    collisions = 0
    # print(vents)
    for vent in vents:
        if vents[vent] > 1:
            collisions += 1
    return collisions, vents

def solve2(cases):
    vents = {}
    for line in cases:
        start = line.points[0]
        end = line.points[1]
        if start.x != end.x and start.y != end.y:
            if start.x > end.x: # sort on x
                s = end
                e = start
            else:
                s = start
                e = end
            print(s.x, s.y, '->', e.x, e.y)
            if s.y < e.y:
                for j in range(e.x - s.x +1):
                    point = (s.x + j, s.y + j)
                    if point not in vents:
                        vents[point] = 1
                    else:
                        vents[point] += 1
            else:
                for j in range(e.x - s.x + 1):
                    point = (s.x + j, s.y - j)
                    if point not in vents:
                        vents[point] = 1
                    else:
                        vents[point] += 1
            
        if start.x == end.x:
            x = start.x
            ends = start.y, end.y
            for i in range(min(ends), max(ends) + 1):
                if (x,i) not in vents:
                    vents[(x,i)] = 1
                else:
                    vents[(x,i)] += 1
        elif start.y == end.y:
            y = start.y
            ends = start.x, end.x
            for i in range(min(ends), max(ends) + 1):
                if (i,y) not in vents:
                    vents[(i,y)] = 1
                else:
                    vents[(i,y)] += 1
    
    collisions = 0
    # print(vents)
    for vent in vents:
        if vents[vent] > 1:
            collisions += 1
    return collisions, vents



def prep(cases):
    lines = []
    for case in cases:
        dots = case.split(' ')
        d1 = dots[0].split(',') # the middle is an arrow
        d2 = dots[2].split(',')

        start = Dot(x = int(d1[0]), y = int(d1[1]))
        end =  Dot(int(d2[0]),int(d2[1]))
        line = Line(start, end)
        lines.append(line)
    return lines

def render(vents):
    # print(vents)
    xs = [v[0] for v in vents]
    ys = [v[1] for v in vents]
    maxX = max(xs) + 1
    maxY = max(ys) + 1
    for i in range(maxX):
        for j in range(maxY):
            if (j, i) not in vents:
                print('.', end = '')
            else:
                print(vents[(j,i)], end = '')
        print()
    print()

if __name__ == '__main__':
    datad = loadData(INPUT)
    testd = loadData(TEST0)

    data = prep(datad)
    test = prep(testd)

    print(test)

    test_results = solve(test)
    
    render(test_results[1])

    if test_results[0] != RESULT0:
        print(test_results[0], 'should be {}'.format(RESULT0))
        exit()

    results = solve(data)

    test_results = solve2(test)
    render(test_results[1])

    if test_results[0] != RESULT1:
        print(test_results[0], 'should be {}'.format(RESULT1))
        exit()
    print("test result matched", test_results[0])

    results = solve2(data)
    print(results[0])
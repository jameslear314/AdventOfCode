INPUT = 'data.9.txt'
TEST0 = 'test.9.0.txt'
RESULT0 = 15
RESULT1 = 1134

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    depths = prep(cases)
    pits = 0
    pitsum = 0
    for y in range(len(depths)):
        for x in range(len(depths[0])):
            depth = depths[y][x]
            adjacents = []
            if y > 0:
                adjacents.append(depths[y - 1][x])
            if y < len(depths) - 1:
                adjacents.append(depths[y + 1][x])
            if x > 0:
                adjacents.append(depths[y][x - 1])
            if x < len(depths[0]) - 1:
                adjacents.append(depths[y][x + 1])
            if depth < min(adjacents):
                pits += 1
                pitsum += depth + 1
    return pitsum

def solve2(cases):
    depths = prep(cases)

    basins = list()
    basins.append(None)
    indextobasin = {}

    for x in range(len(depths)): # Yes, I know I'm flipping the directions. X is now vertical.
        print(x)
        for y in range(len(depths[0])):
            print(y)
            index = (x,y)
            if depths[x][y] == 9:
                indextobasin[(x,y)] = None
            else:
                if index not in indextobasin:
                    basin = mapBasin(depths, x, y)
                    # print(basin)
                    basins.append(basin)
                    for index in basin:
                        indextobasin[index] = basin

    sizes = [len(b) for b in basins if b]
    sizes.sort()
    for basin in basins:
        print(basin)
    print(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]

def adjacents(depths, index):
    x = index[0]
    y = index[1]

    xm1 = x - 1
    xp1 = x + 1
    ym1 = y - 1
    yp1 = y + 1

    adjacent = []

    if xm1 > - 1:
        adjacent.append((xm1, y))
    if ym1 > -1 :
        adjacent.append((x, ym1))
    if xp1 < len(depths):
        adjacent.append((xp1, y))
    if yp1 < len(depths[0]):
        adjacent.append((x, yp1))
    
    return adjacent

def mapBasin(depths, x, y):
    basin = set()
    start = (x,y)
    maybes = [start]

    while len(maybes):
        nexts = []
        for index in maybes:
            print("index and its adjacents", index)

            adjacent = adjacents(depths, index)
            for maybe in adjacent:
                if maybe not in basin:
                    x = maybe[0]
                    y = maybe[1]
                    if depths[x][y] != 9:
                        nexts.append(maybe)
                        basin.add(maybe)
        maybes = nexts
    return basin

def prep(cases):
    depths = []
    for case in cases:
        depth = []
        for char in case:
            depth.append(int(char))
        depths.append(depth)
    return depths

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
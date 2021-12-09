INPUT = 'data.9.txt'
TEST0 = 'test.9.0.txt'
RESULT0 = 15
RESULT1 = 5

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
    return None

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
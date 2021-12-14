INPUT = 'data.13.txt'
TEST0 = 'test.13.0.txt'
RESULT0 = 7
RESULT1 = 5

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    grid, folds = prepgrid(cases)
    print(grid)
    fold = folds[0]
    if fold[0] == 'x': # This transformation is not necessary, except that I always invert grids
        dimension = 'c'
    else:
        dimension = 'r'
    
    newgrid = []
    if dimension == 'r':
        for i in range(len(grid)):
            



def solve2(cases):
    return None

def prepgrid(cases):
    points, folds = prep(cases)
    xs = [int(p[0]) for p in points]
    ys = [int(p[1]) for p in points]

    grid = []
    for _ in range(max(xs) + 1):
        row = []
        for __ in range(max(ys) + 1):
            row.append(0)
        grid.append(row)

    for point in points:
        grid[int(point[0])][int(point[1])] = 1
    return grid, folds

def prep(cases):
    points = []
    folds = []
    for case in cases:
        if ',' in case:
            values = case.split(',')
            points.append((values[0], values[1]))
        elif 'fold' in case:
            words = case.split(' ')
            instruction = words[-1]
            folds.append((instruction[0], instruction[1]))
    return points, folds

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
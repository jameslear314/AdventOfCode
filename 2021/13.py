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
    return None

def solve2(cases):
    return None

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
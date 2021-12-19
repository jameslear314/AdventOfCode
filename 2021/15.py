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

def solve(cases):
    grid = prep(cases)


def solve2(cases):
    return None


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
    grid = prep(test)

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
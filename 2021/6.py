INPUT = 'data.6.txt'
TEST0 = 'test.6.0.txt'
RESULT0 = 5934
RESULT1 = 26984457539

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases, count):
    ages = cases[0].split(',')
    ages = [int(a) for a in ages]
    print(ages)
    depth = 9

    aged = {}
    for i in range(depth):
        aged[i] = 0
    for age in ages:
        aged[age] += 1

    newaged = {}
    for i in range(count):
        newaged = {}
        for j in range(depth):
            newaged[j] = 0
        for j in range(depth):
            if j == 0:
                newaged[8] += aged[j]
                newaged[6] += aged[j]
            else:
                newaged[j - 1] += aged[j]
        aged = newaged

    result = 0
    for a in aged:
        result += aged[a]

    return result

    

def solve2(cases, count):
    return solve(cases, count)

if __name__ == '__main__':
    data = loadData(INPUT)
    test = loadData(TEST0)

    print(test)

    test_results = solve(test, 80)
    if test_results != RESULT0:
        print(test_results, 'should be {}'.format(RESULT0))
        exit()
    print('results', test_results)

    results = solve(data, 80)
    print(results)

    count = 256
    test_results = solve2(test, count)

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve2(data, count)
    print(results)
INPUT = 'data.1.txt'
TEST0 = 'test.1.0.txt'
RESULT0 = 7
RESULT1 = 5

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [int(l.strip()) for l in lines]
    return lines

def solve(cases):
    val = cases[0]
    result = 0
    for case in cases[1:]:
        if case > val:
            result += 1
        val = case
    return result

def solve2(cases):
    end = len(cases)
    start = 2
    result = 0
    for i in range(end):
        if nexts(cases, i + start) > prior(cases, i + start):
            result += 1
    return result

def prior(cases, index):
    values = cases[index - 2 : index + 1]
    return sum(values)
def nexts(cases, index):
    values = cases[index - 1 : index + 2]
    return sum(values)

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
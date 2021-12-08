INPUT = 'data.8.txt'
TEST0 = 'test.8.0.txt'
RESULT0 = 26
RESULT1 = 5

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    patterns = {}
    for case in cases:
        pattern, value = case.split('|')
        patterns[pattern.strip()] = value.strip()
    
    allElems = []
    for pattern in patterns:
        value = patterns[pattern]
        elem = value.split(' ')
        elems = [e for e in elem if e]
        allElems += elems
    
    selected = [a for a in allElems if len(a) in [2, 4, 3, 7]]
    return len(selected)
    


def solve2(cases):
    return None

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
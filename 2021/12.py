INPUT = 'data.12.txt'
TEST0 = 'test.12.0.txt'
TEST1 = 'test.12.1.txt'
TEST2 = 'test.12.2.txt'
RESULT00 = 10
RESULT01 = 19
RESULT02 = 226
RESULT1 = 5

start = 'start'
end = 'end'

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    return None

def solve2(cases):
    return None

def prep(links):
    graph = []
    for link in links:
        ends = link.split('-')
        graph.append((ends[0], ends[1]))
    
    map = {}
    for grap in graph:
        for item in grap:
            if item not in map:
                map[item] = []
        map[grap[0]] = grap[1]
        map[grap[1]] = grap[0]
    return map

if __name__ == '__main__':
    data = loadData(INPUT)
    test = loadData(TEST0)
    test1 = loadData(TEST1)
    test2 = loadData(TEST2)

    print(test)

    test = 0
    for pair in [(test, RESULT00), (test1, RESULT01), (test2, RESULT02)]:
        print("Test number", test, end=": ")
        test_results = solve(pair[0])
        if test_results != pair[1]:
            print(test_results, 'should be {}'.format(pair[1]))
            exit()
        print('results', test_results)
        test += 1

    results = solve(data)
    print(results)

    test_results = solve2(test)

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve2(data)
    print(results)
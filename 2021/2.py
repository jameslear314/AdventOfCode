INPUT = 'data.2.txt'
TEST0 = 'test.2.0.txt'
RESULT0 = 150
RESULT1 = 900

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    output = []
    for line in lines:
        action, number = line.split(' ')
        number = int(number)
        action = action[0]
        output.append((action, number))
    
    return output

def solve(cases):
    depth, distance = 0, 0
    for case in cases:
        value = case[1]
        action = case[0]
        if action == 'f':
            distance += value
        elif action == 'd':
            depth += value
        elif action == 'u':
            depth -= value
    return depth * distance

def solve2(cases):
    depth, distance, aim = 0, 0, 0
    for case in cases:
        value = case[1]
        action = case[0]
        if action == 'f':
            distance += value
            depth += aim * value
        elif action == 'd':
            aim += value
        elif action == 'u':
            aim -= value
    return depth * distance


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
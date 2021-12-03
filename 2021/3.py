INPUT = 'data.3.txt'
TEST0 = 'test.3.0.txt'
RESULT0 = 198
RESULT1 = 5

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    gamma_v = gamma_value(cases)
    gamma = 0
    epsilon = 0

    base = 1
    for i in range(len(gamma_v)):
        gamma_d = gamma_v[-1 - i] # start at the final int
        if gamma_d:
            epsilon_d = 0
        else:
            epsilon_d = 1
        gamma += base * gamma_d
        epsilon += base * epsilon_d
        base *= 2
        
    return gamma * epsilon

def solve2(cases):
    return None

def gamma_value(cases):
    tally = []
    for i in range(len(cases[0])):
        tally.append(0)
    print("Starting with", tally, "of length", len(tally))
    for case in cases:
        for i in range(len(case)):
            if int(case[i]):
                tally[i] += 1
    print("ending tally,", tally)
    result = []
    for i in range(len(tally)):
        if tally[i] > len(cases) / 2.0:
            result.append(1)
        else:
            result.append(0)
    print("gamma", result)
    return result

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
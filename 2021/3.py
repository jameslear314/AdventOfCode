INPUT = 'data.3.txt'
TEST0 = 'test.3.0.txt'
RESULT0 = 198
RESULT1 = 230 # Test case should be 230, but the description is incorrect

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
    gamma_cases = cases[:] #oxy
    epsilon_cases = cases[:] #co2
    # for case in cases:
    #     gamma_cases.append(case)
    #     epsilon_cases.append(case)
    tally = tally_v(cases)

    
    for i in range(len(tally)):
        print("round", i)
        gamma_tally = tally_v(gamma_cases)
        epsilon_tally = tally_v(epsilon_cases)
        print(len(gamma_cases), len(epsilon_cases))
        gamma_ratio = (gamma_tally[i] + 0.0)/len(gamma_cases)
        epsilon_ratio = (epsilon_tally[i] + 0.0)/len(epsilon_cases)
        
        if gamma_ratio < 0.5:
            gamma_key = 0
        else:
            gamma_key = 1
        if epsilon_ratio < 0.5:
            epsilon_key = 1
        else:
            epsilon_key = 0

        print("gamma", gamma_key, "epsilon", epsilon_key, "gamma_ratio", gamma_ratio, "epsilon_ratio", epsilon_ratio)
        if len(gamma_cases) > 1:
            gamma_cases = [c for c in gamma_cases if int(c[i]) == gamma_key]
        if len(epsilon_cases) > 1:
            epsilon_cases = [c for c in epsilon_cases if int(c[i]) == epsilon_key]
        print("gamma_case_len", len(gamma_cases), "epsilon_case_len", len(epsilon_cases))
        print("gamma_Cases", gamma_cases)
        print("epsilon_cases", epsilon_cases)


    gamma = decimal(gamma_cases[0])
    epsilon = decimal(epsilon_cases[0])
    print(gamma, gamma_cases[0], epsilon, epsilon_cases[0])
    return gamma * epsilon
    
def decimal(tally):
    gamma = 0

    base = 1
    for i in range(len(tally)):
        gamma_d = tally[-1 - i] # start at the final int
        gamma += base * int(gamma_d)
        base *= 2
    return gamma
    

def tally_v(cases):
    tally = []
    for i in range(len(cases[0])):
        tally.append(0)
    for case in cases:
        for i in range(len(case)):
            if int(case[i]):
                tally[i] += 1
    return tally

def gamma_value(cases):
    tally = tally_v(cases)
    result = []
    for i in range(len(tally)):
        if tally[i] > len(cases) / 2.0:
            result.append(1)
        else:
            result.append(0)
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

    data = loadData(INPUT)
    test = loadData(TEST0)
    test_results = solve2(test)

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve2(data)
    print(results)
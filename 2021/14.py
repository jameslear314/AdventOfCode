from typing import NewType


INPUT = 'data.14.txt'
TEST0 = 'test.14.0.txt'
RESULT0 = 1588
RESULT1 = 5

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases, itercount):
    current, transforms = prep(cases)
    
    next = []
    for c in range(itercount):
        print(c, len(current))
        for i in range(len(current) -1):
            pair = ''.join(current[i:i+2])
            next.append(pair[0])
            if pair in transforms:
                next.append(transforms[pair])
        next.append(current[-1])
        current = next
        next = []
    
    counts = {}
    for char in current:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    values = counts.values()
    return max(values) - min(values)


def solve2(cases):
    return None

def prep(cases):
    input = cases[0]
    output = []
    for char in input:
        output.append(char)

    transforms = {}
    maps = cases[2:]
    for map in maps:
        elems = map.split(' ')
        transforms[elems[0]] = elems[-1]
    
    return output, transforms
    

if __name__ == '__main__':
    data = loadData(INPUT)
    test = loadData(TEST0)

    print(test)

    test_results = solve(test, 10)
    if test_results != RESULT0:
        print(test_results, 'should be {}'.format(RESULT0))
        exit()
    print('results', test_results)

    results = solve(data, 10)
    print(results)

    test_results = solve(test, 40)

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve(data, 40)
    print(results)
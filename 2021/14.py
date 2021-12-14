from typing import NewType


INPUT = 'data.14.txt'
TEST0 = 'test.14.0.txt'
RESULT0 = 1588
RESULT1 = 2188189693529

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


def solve2(cases, itercount):
    current, transforms = prep(cases)

    currentcount = {}
    for i in range(len(current) - 1):
        key = current[i] + current[i+1]
        if key not in currentcount:
            currentcount[key] = 1
        else:
            currentcount[key] += 1
    print(currentcount)

    for i in range(itercount):
        nextcount = {}
        childcount = {}
        keys = currentcount.keys()
        for key in keys:
            if key in transforms:
                keyA = key[0]+transforms[key]
                keyB = transforms[key]+key[1]
                for keyc in keyA, keyB:
                    if keyc not in childcount:
                        childcount[keyc] = currentcount[key]
                    else:
                        childcount[keyc] += currentcount[key]
            else:
                if key not in childcount:
                    childcount[key] = currentcount[key]
                else:
                    childcount[key] += currentcount[key]
        for key in childcount:
            if key not in nextcount:
                nextcount[key] = childcount[key]
            else:
                nextcount[key] += childcount[key]
        currentcount = nextcount

    assigns = {}
    for key in currentcount:
        for char in key[0], key[1]:
            if char not in assigns:
                assigns[char] = currentcount[key]
            else:
                assigns[char] += currentcount[key]
    
    values = assigns.values()
    return max(values) - min(values)

def expand(string, trans, counts, level):
    if level == 0:
        record(string[0], string[1], counts)
    else:
        key = ''.join(string)
        if key not in trans:
            record(string[0], string[1], counts)
        else:
            mid = trans[key]
            expand([string[0], mid], trans, counts, level - 1)
            expand([mid, string[1]], trans, counts, level - 1)

def record(s1, s2, counts):
    for char in (s1, s2):
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1


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

    test_results = solve2(test, 40)

    # if test_results != RESULT1:
    #     print(test_results, 'should be {}'.format(RESULT1))
    #     print('test is bigger than expected:', test_results >= RESULT1)
    #     print(test_results/2)
    #     print(test_results - RESULT1)

    #     exit()

    results = solve2(data, 40)
    print(results)
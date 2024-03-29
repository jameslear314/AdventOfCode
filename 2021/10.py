INPUT = 'data.10.txt'
TEST0 = 'test.10.0.txt'
RESULT0 = 26397
RESULT1 = 288957

equal = ['{}', '[]', '()', '<>']
equalmap = {}
for sign in equal:
    equalmap[sign[0]] = sign[1]
    equalmap[sign[1]] = sign[0]

scorelookup = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completelookup = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    total = 0
    for case in cases:
        badchar = None
        proceed = True
        stack = []
        for char in case:
            if proceed:
                if char in '{([<':
                    stack.append(char)
                elif char in '})]>':
                    if stack[-1] != equalmap[char]:
                        proceed = False
                        badchar = char
                    else:
                        stack = stack[:-1]
        if badchar:
            total += scorelookup[badchar]
    return total

def solve2(cases):
    scores = []
    for case in cases:
        score = 0
        badchar = None
        proceed = True
        stack = []
        for char in case:
            if proceed:
                if char in '{([<':
                    stack.append(char)
                elif char in '})]>':
                    if stack[-1] != equalmap[char]:
                        proceed = False
                        badchar = char
                    else:
                        stack = stack[:-1]
        if not badchar:
            for i in range(len(stack)):
                score *= 5
                score += completelookup[stack[-i - 1]]
        if score > 0:
            scores.append(score)
    scores.sort()
    return scores[int(len(scores) / 2)]

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
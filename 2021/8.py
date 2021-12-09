INPUT = 'data.8.txt'
TEST0 = 'test.8.0.txt'
RESULT0 = 26
RESULT1 = 61229

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
    patterns = {}
    for case in cases:
        pattern, value = case.split('|')
        patterns[pattern.strip()] = value.strip()
    
    values = []
    for pattern in patterns:
        values.append(calculateVal(pattern, patterns[pattern]))
    print(values)
    return sum(values)

def calculateVal(pattern, value):
    inputs = pattern.split(' ')
    input = [i for i in inputs if i]
    outputs = value.split(' ')
    output = [o for o in outputs if o]

    charsInVal = calcCharsInVal(input)

    for char in charsInVal:
        digit = charsInVal[char]
        charsInVal[char] = sortChars(digit)

    results = []
    for o in output:
        o = sortChars(o)
        found = False
        for char in charsInVal:
            if o == charsInVal[char]:
                found = True
                results.append(char)
        if not found:
            print("WTF, should have found the digit")
            print(o)
            print(charsInVal)

    result = 0
    multiplier = 1
    for i in range(len(results)):
        result += multiplier * results[-i - 1]
        multiplier *= 10
    return result

def sortChars(digit):
    
    chars = []
    for c in digit:
        chars.append(c)
    chars.sort()
    return ''.join(chars)

def calcCharsInVal(input):
    charsinval = {}
    leftovers = []

    lengths = {
        6: [0,6,9],
        5: [2,3,5]
    }

    for put in input:
        length = len(put)
        if length == 2:
            charsinval[1] = put
        elif length == 4:
            charsinval[4] = put
        elif length == 3:
            charsinval[7] = put
        elif length == 7:
            charsinval[8] = put
        else:
            leftovers.append(put)

    zsn = [l for l in leftovers if len(l) == 6]
    ttf = [l for l in leftovers if len(l) == 5]

    for char in zsn:
        found = False
        for c in charsinval[1]:
            if c not in char:
                charsinval[6] = char
                found = True
        
        if not found:
            for c in charsinval[4]:
                if c not in char:
                    charsinval[0] = char
                    found = True
        if not found:
            charsinval[9] = char

    for char in ttf:
        found = False
        if charsinval[1][0] in char and charsinval[1][1] in char:
            charsinval[3] = char
            found = True
        
        if not found:
            count = 0
            for c in char:
                if c in charsinval[6]:
                    count += 1
            if count == 5:
                charsinval[5] = char
            elif count == 4:
                charsinval[2] = char
            else:
                print("WTF, failed to find the chars")
                keys = list(charsinval.keys())
                print(count)
                keys.sort() 
                print(keys)
                print(input)
                exit()
    return charsinval


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
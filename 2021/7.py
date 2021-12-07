INPUT = 'data.7.txt'
TEST0 = 'test.7.0.txt'
RESULT0 = 37
RESULT1 = 168
ANSWERISNOT = 116,296,231

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    strings = cases.split(',')
    positions = [int(s) for s in strings]
    positions.sort()
    
    results = []

    # guess = int(positions[len(positions/2)])

    for i in range(min(positions), max(positions)):
        results.append(consume(positions,i))

    return min(results)
    
def consume(positions, guess):
    total = 0
    for pos in positions:
        total += abs(pos-guess)
    return total

def consumemore(positions, guess):
    total = 0
    keyMap = {}
    for pos in positions:
        key = abs(pos - guess)
        if key in keyMap:
            total += keyMap[key]
            continue
        newval = key
        for i in range(key):
            newval += i
        keyMap[key] = newval
        total += newval
    return total
        


def solve2(cases):
    strings = cases.split(',')
    positions = [int(s) for s in strings]
    positions.sort()
    
    guessResult = max(consumemore(positions, min(positions)), consumemore(positions, max(positions))) + 1
    newResult = guessResult - 1
    i = 0 #index
    while newResult <= guessResult:
        newResult = consumemore(positions, positions[i])
        if newResult < guessResult:
            guessResult = newResult
        i += 1

    guessResult = newResult
    guess = positions[i]
    
    print(guess, consumemore(positions, guess))
    guess = positions[i -1]
    while newResult <= guessResult:
        newResult = consumemore(positions, guess)
        print(guess, newResult)
        if newResult < guessResult:
            guessResult = newResult
        guess -= 1
    print(guess, consumemore(positions, guess))
    
    

    return guessResult

def confirm(start, guess, cost):
    val = consumemore([start], guess)
    if val != cost:
        print(val, "should have been", cost)
    else:
        print(val, "passed")

def confirmList(pos, guess, cost):
    val = consumemore(pos, guess)
    
    if val != cost:
        print(val, "should have been", cost)
    else:
        print(val, "passed")


if __name__ == '__main__':
    data = loadData(INPUT)
    test = loadData(TEST0)

    print(test[0])

    test_results = solve(test[0])
    if test_results != RESULT0:
        print(test_results, 'should be {}'.format(RESULT0))
        exit()
    print('results', test_results)

    results = solve(data[0])
    print(results)

    
    strings = test[0].split(',')
    positions = [int(s) for s in strings]
    positions.sort()

    confirm(16, 5, 66)
    confirm(1,5,10)
    confirm(2,5,6)
    confirm(0,5,15)
    confirm(4,5,1)
    confirm(7,5,3)
    confirm(1,5,10)
    confirm(14,5,45)
    confirmList(positions, 5, 168)
    confirmList(positions, 2, 206)

    test_results = solve2(test[0])

    if test_results != RESULT1:
        print(test_results, 'should be {}'.format(RESULT1))
        exit()

    results = solve2(data[0])
    print(results)
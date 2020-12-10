import math
INPUT = '''77
58
25
92
14
154
105
112
147
63
84
109
24
129
49
102
130
128
134
88
95
70
80
4
153
17
145
122
39
117
93
65
3
2
139
101
148
37
27
1
87
64
23
59
42
146
43
151
116
46
115
118
131
94
19
33
12
107
10
7
73
78
53
11
135
79
60
32
141
31
140
98
136
72
38
152
30
74
106
50
13
26
155
67
20
66
91
56
34
125
52
51
18
108
57
81
119
71
144
'''

TEST = '''16
10
15
5
1
11
7
19
6
12
4
'''

TEST2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''

RUNS = 0
TOTAL = 0
def solve(cases):
    
    cases = cases.split('\n')
    adapts = [int(i) for i in cases if i]
    adapts.sort()

    diffs = {1: 1, 3:1}
    for i in range(len(adapts)):
        if i == 0:
            last = adapts[i]
            continue
        diff = adapts[i] - adapts[i-1]
        diffs[diff] += 1

    return diffs[1] * diffs[3]



def solve2(cases):
    max = solve(cases)
    cases = cases.split('\n')
    cases = [int(i) for i in cases if i]

    count = 1
    length = len(cases)
    for i in range(length):
        delta = 1
        while length - i - 1 - delta >= 0 and cases[length - i - 1] - cases[length - i - 1 - delta] <= 3:
            delta += 1
        count += delta
    return count

def valid(numbers):
    first = numbers[0]
    for number in numbers[1:]:
        # new = number - first
        # print(new)
        if number - first not in [1, 3]:
            return False
        first = number
    return True

def solve3(cases):
    cases = cases.split('\n')
    cases = [int(i) for i in cases if i]
    cases.sort()

    count = 1
    for i in range(1, len(cases) - 1):
        if valid(cases[:i] + cases[i + 1:]):
            count # is what. Not sure how to solve this.

def brute(cases, valids = 1):

    if not valid(cases):
        return 0
    now_valids = 1
    for i in range(len(cases)):
        new = cases[:i] + cases[i + 1:]
        if valid(new):
            now_valids += brute(cases, 1)
    return valids + now_valids 

def combine(numbers, final):
    initial = 0
    # if not valid([initial] + numbers + [max(numbers) + 3]):
    #     print("Seriously, should be valid.")
    #     exit()

    length = len(numbers)
    total = 1
    for i in range(length):
        j = 0
        for j in range(1, length - i):
            if numbers[i + j] - numbers[i] > 3:
                break
        if j > 1:
            if j == 2:
                total *= j
            if j == 3:
                total *= j * 2
        if i < length:
            total += combine(numbers[:i] + numbers[i + 1:], final)
    global RUNS
    global TOTAL
    RUNS += 1
    if total > TOTAL:
        TOTAL = total
        print(RUNS, TOTAL, length)
    return total

def addify(numbers, cache, i):
    #don't recalculcate
    if i in cache:
        return cache[i]
    #break the recursion
    if i + 1 == len(numbers):
        return 1
    
    result = 0
    #limit the search to possible values in a sorted list
    for j in range(i + 1, i + 3):
        if j < len(numbers) and numbers[j] - 3 <= numbers[i]:
            result += addify(numbers, cache, j)
    cache[j]  = result

    return result

def calculate(cases):
    tests = cases.split('\n')
    tests = [int(i) for i in tests if i]
    tests.sort()
    if not valid(tests):
        print("should be valid")
        exit()

    # return brute(tests, 1)

    # final = solve(cases)
    # return combine(tests, final)

    return addify(tests, {}, 0)


if __name__ == '__main__':
    test_results = solve(TEST)
    if test_results != 35:
        print(test_results, 'should be 35')
        exit()
    print('results', test_results)
    test_results = solve(TEST2)
    if test_results != 22 * 10:
        print(test_results, 'should be 22 * 10')
        exit()
    print('results', test_results)

    results = solve(INPUT)
    print(results)
    if results != 2059:
        print(results, "should be 2059")
        exit()

    test_results = calculate(TEST)
    if test_results != 8:
        print(test_results, 'should be 8')
        exit()
    print('results', test_results)
    test_results = calculate(TEST2)
    if test_results != 19208:
        print(test_results, 'should be 19208')
        exit()
    print('results', test_results)

    results = calculate(INPUT)
    print(results)
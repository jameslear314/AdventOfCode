import math
from timeit import default_timer as timer

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

INPUT2 = '''77
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
    cache[i] = result

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

def combinatoric_valid(subset, start, finish):
    if len(subset) < 2: # This should have been caught by start != finish and start and finish in subset. Odd?
        return False
    for i in range(1, len(subset)):
        diff = subset[i] - subset[i - 1]
        if diff < 1 or diff > 3 or start not in subset or finish not in subset:
            return False
    return True

def combinatoric(numbers):
    length = len(numbers)
    print(' numbers:', numbers, 'start', numbers[0], 'finish', numbers[-1])
    total = 1 #When all numbers are included
    for i in range(1, length - 1): #at least 3 numbers are in the range
        subset = numbers[:i] + numbers[i + 1:] #check the range when this index is skipped
        if combinatoric_valid(subset, numbers[0], numbers[-1]):
            print('i subset:', subset)
            total += 1
            for j in range(1, length - i):
                subset = numbers[:i] + numbers[i+1:i+j] + numbers[i+j+1:]
                if combinatoric_valid(subset, numbers[0], numbers[-1]):
                    print('j subset:', subset)
                    total += 1
                    for k in range(1, length - i - j):
                        subset = numbers[:i] + numbers[i+1:i+j] + numbers[i+j+1:i+j+k] + numbers[i+j+k+1:]
                        if combinatoric_valid(subset, numbers[0], numbers[-1]):
                            print('k subset:', subset)
                            total += 1
    print('   total:', total)
    return total


def numberify(input):
    input = input.split('\n')
    input = [int(n) for n in input if n]
    # Problem specific kink: 0 must be included
    if 0 not in input:
        input = [0] + input
    input.sort()
    return input


def prepare_combinatoric(input):
    diffs = set()
    ranges = []
    start = 0
    for i in range(1, len(input)):
        diff = input[i] - input[i - 1]
        diffs.add(diff)
        if diff >= 3:
            # Segment the input into smaller chunks for combinatorics
            ranges.append((start, i))
            start = i
    return diffs, ranges

def solve_part2_a(numbers, groups):
    count = 1
    for group in groups:
        subset = numbers[group[0]:group[1]]
        count *= combinatoric(subset)
    return count

def sum_combinations(numbers):
    start = numbers[0]
    finish = numbers[-1]
    combinations = [[numbers[0]]]
    for number in numbers[1:]:
        new_combinations = combinations[:]
        for combination in combinations:
            new_combinations.append(combination + [number])
        combinations = new_combinations[:]

    valids = [c for c in combinations if start in c and finish in c]
    if len(numbers) == 1:
        return len(valids)
    results = [c for c in valids if max(prepare_combinatoric(c)[0]) <= 3]
    return len(results)

def sum_combinations_brute(numbers):
    overall_start_time = timer()
    start = numbers[0]
    finish = numbers[-1]
    combinations = [[numbers[0]]]
    group = 0
    last_duration = 0
    for number in numbers[1:]:
        group += 1
        start_time = timer()
        new_combinations = combinations[:]
        for combination in combinations:
            new_combinations.append(combination + [number])
        combinations = new_combinations[:]
        valid_combinations = [c for c in combinations if len(c) == 1 or max(prepare_combinatoric(c)[0]) <= 3]
        combinations = valid_combinations[:]
        lengths = [len(c) for c in combinations]
        end_time = timer()
        group_duration = end_time - start_time
        overall_duration = end_time - overall_start_time
        duration_power = math.pow(group_duration - last_duration, len(numbers) - group)
        print("Group", group, "had", len(valid_combinations), "valid combinations, took", overall_duration, "seconds")

    valids = [c for c in combinations if start in c and finish in c]
    results = [c for c in valids if max(prepare_combinatoric(c)[0]) <= 3]
    return len(results)

def solve_part2_b(numbers, groups):
    count = 1
    for group in groups:
        subset = numbers[group[0]:group[1]]
        print(subset, count)
        count *= sum_combinations(subset)
    return count

def solve_part2(numbers, groups):
    return sum_combinations_brute(numbers)

if __name__ == '__main__':
    test_results = solve(TEST)
    if test_results != 35:
        print(test_results, 'should be 35')
        exit()
    print('part 1 test 1 results', test_results)
    test_results = solve(TEST2)
    if test_results != 22 * 10:
        print(test_results, 'should be 22 * 10')
        exit()
    print('part 1 test 2 results', test_results)

    results = solve(INPUT)
    print('part 1 results', results)
    if results != 2059:
        print(results, "should be 2059")
        exit()

    numbers = numberify(INPUT)
    input_diff, input_ranges = prepare_combinatoric(numbers)
    test1_numbers = numberify(TEST)
    test1_diff, test1_ranges = prepare_combinatoric(test1_numbers)
    test2_numbers = numberify(TEST2)
    test2_diff, test2_ranges = prepare_combinatoric(test2_numbers)
    results2 = -1
    is_valid = True

    test_results = solve_part2(test1_numbers, test1_ranges)
    if test_results != 8:
        print("part 2 test 1 should be 8 but was", test_results)
        is_valid = False
    test_results2 = solve_part2(test2_numbers, test2_ranges)
    if test_results2 != 19208:
        print("part 2 test 2 should be 19208 but was", test_results2)
        is_valid = False
    if is_valid:
        results2 = solve_part2(numbers, input_ranges)
    print("part 2 results:", results2)
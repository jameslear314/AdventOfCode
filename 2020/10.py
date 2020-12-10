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

    count = 1
    length = len(cases)
    for i in range(length):
        delta = 1
        while cases[length - i] - cases[length - i - delta] <= 3:
            delta += 1
        count *= delta
    return count



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

    
    test_results = solve2(TEST)
    if test_results != 8:
        print(test_results, 'should be 8')
        exit()
    print('results', test_results)
    test_results = solve2(TEST2)
    if test_results != 19208:
        print(test_results, 'should be 19208')
        exit()
    print('results', test_results)

    results = solve2(INPUT)
    print(results)
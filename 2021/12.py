INPUT = 'data.12.txt'
TEST0 = 'test.12.0.txt'
TEST1 = 'test.12.1.txt'
TEST2 = 'test.12.2.txt'
RESULT00 = 10
RESULT01 = 19
RESULT02 = 226
RESULT10 = 36
RESULT11 = 103
RESULT12 = 3509


start = 'start'
end = 'end'

def loadData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
    lines = [l.strip() for l in lines]
    return lines

def solve(cases):
    print(cases)
    map = prep(cases)
    print(map)
    paths = []

    for dest in map[start]:
        paths.append([start, dest]) # [start, interim, end]

    pathcount = 0
    round = 0
    while len(paths) != pathcount:
        currents = paths[:]
        nexts = []
        for i in range(len(currents)):
            for dest in map[currents[i][-1]]:
                if currents[i][-1] == end or (dest != dest.upper() and dest in currents[i]):
                    if currents[i] not in nexts:
                        nexts.append(currents[i])
                    continue
                working = currents[i][:]
                working.append(dest)
                nexts.append(working)
        pathcount = len(paths)
        paths = nexts
        print(round, pathcount)
        round += 1
    
    candidates = [','.join(p) for p in paths if p[-1] == end]
    return len(set(candidates))

def solve2(cases):
    print(cases)
    map = prep(cases)
    print(map)
    paths = []

    for dest in map[start]:
        paths.append(','.join([start, dest])) # [start, interim, end]

    pathcount = 0
    round = 0
    while len(paths) != pathcount:
        currents = paths[:]
        nexts = []
        for i in range(len(currents)):
            path = currents[i].split(',')
            debug = False
            if currents[i] == 'start,A,b,A':
                debug = True
                
            if path[-1] == start or path[-1] == end:
                nexts.append(currents[i])
                continue
            dests = map[path[-1]]
            for dest in dests:
                if debug and dest == 'b':
                    debug = True
                if dest == start:
                    continue
                svisits = {}
                small = dest != dest.upper()
                for d in path:
                    if d != d.upper():
                        if d not in svisits:
                            svisits[d] = 1
                        else:
                            svisits[d] += 1
                if small:
                    if max(svisits.values()) >= 2 and dest in path:
                        continue
                
                if debug and dest == 'b':
                    debug = True
                testpath = currents[i] + ',' + dest
                nexts.append(testpath)

        pathcount = len(paths)
        paths = nexts
        print('round', round, 'has', pathcount)
        round += 1

    candidates = [p for p in paths if p[-3:] == end]
    print(candidates)
    return len(set(candidates))

def prep(links):
    graph = []
    for link in links:
        ends = link.split('-')
        graph.append((ends[0], ends[1]))
    
    map = {}
    for grap in graph:
        for item in grap:
            if item not in map:
                map[item] = []
        map[grap[0]].append(grap[1])
        map[grap[1]].append(grap[0])
    for key in map:
        map[key] = list(set(map[key]))
    return map

if __name__ == '__main__':
    data = loadData(INPUT)
    test0 = loadData(TEST0)
    test1 = loadData(TEST1)
    test2 = loadData(TEST2)

    # print(test0)

    # test = 0
    # for pair in [(test0, RESULT00), (test1, RESULT01), (test2, RESULT02)]:
    #     print("Test number", test, end=": ")
    #     test_results = solve(pair[0])
    #     if test_results != pair[1]:
    #         print(test_results, 'should be {}'.format(pair[1]))
    #         exit()
    #     print('results', test_results)
    #     test += 1

    # results = solve(data)
    # print(results)

    test = 0
    for pair in [(test0, RESULT10), (test1, RESULT11), (test2, RESULT12)]:
        print("Test number", test, end=": ")
        test_results = solve2(pair[0])
        if test_results != pair[1]:
            print(test_results, 'should be {}'.format(pair[1]))
            exit()
        print('results', test_results)
        test += 1

    results = solve2(data)
    print(results)
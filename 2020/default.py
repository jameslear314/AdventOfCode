INPUT = '''
'''

TEST = '''
'''

def solve(cases):
    return None

def solve2(cases):
    return solve(cases)

if __name__ == '__main__':
    test_results = solve(TEST)
    if test_results != 5:
        print(test_results, 'should be 5')
        exit()
    print('results', test_results)

    results = solve(INPUT)
    print(results)

    # test_results = solve2(TEST)
    # if test_results != 8:
    #     print(test_results, 'should be 8')
    #     exit()

    # results = solve2(INPUT)
    # print(results)
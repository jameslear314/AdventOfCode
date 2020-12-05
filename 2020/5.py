import math
TESTS = {
    'BFFFBBFRRR': (70, 7, 567),
    'FFFBBBFRRR': (14, 7, 119),
    'BBFFBBFRLL': (102, 4, 820)
}

INPUT = '''BFBBBFBLRR
BBFFFFFLRR
BFBFBFFRLR
FBBBBFFLLL
BFBBBBFRRL
FFBFFBFRLR
FFFBFBBRRL
FBFBBFBLRL
FBFFFBFLLR
FFBBFBBLLL
FBFBBFFRLL
FFBFFBFLRL
FFBFBFFRRR
BFFFFBBLRR
FFBFFBFRRL
FFBFBFFLRL
BBFFFFFRLL
FFFBFBBRRR
FBFBFBBLLR
FBFBFBFLLR
BFBFBFFRLL
FFFBFFBRLL
BBFFFBFLRL
BFBFBFBLLR
FFFFBBBRLL
FFBBBFFLRL
FBFFBFBRLR
FFBFBBFLLR
FBFBFFFRRL
BFBBFBBLRR
BFBFFFBRRR
BFFBBBFRLL
FFBFFFFRRL
FFFFBBFLRL
BBFFFBBRLR
BFFBFBBRRL
BFFFFFBLRR
FBFFFFBLLL
FFBFBBFLLL
BFBBBFBRRR
BBFFFBFLLR
FBBBFFFRRL
BFBBBBBLLL
BFBFFFBRLR
FFBBFBBLRR
FBFBFFFLLL
BFBBBFBRLL
BFFBFBFRRL
BFBFBFFRRR
FBBFFFFLLR
FFBBBFFLLL
BFFBFBBRRR
FFBFBFBRRR
FFFBBFFRRR
FFBBFBFRLR
FBBBFBFRRR
FFBFFBFRLL
BFBBBFFRLR
FBFFFFFRLR
BFBBBFBRRL
FBFFBFBRRL
FFBFBBFRLL
FFFBBBBLLL
FFBBBFBLLR
FFBBFFBRRR
FFBBBBFRRR
FFBFBBBLRL
FBBBBBFLLR
BFBFBBFLLR
FFFBBBFRLL
BFBFFBBRRL
FBFBBFBLLL
FBFFBBFLRR
FBBBFBFLRL
FFBBFBFRLL
FFBBBFFRRR
BFFBBBBRLR
FFBFFBBRLL
FBFBFBBRRL
FFBFFBFLLR
FBFBFFBLLR
FBFBBFFLLL
FBFBBFBLLR
FBBFBBFRLL
BFFFBFFRLL
FFBBBFFRLL
FBFBBFBRRR
BFFBBFFRLL
FFBFBBFRRR
FBBFFFFRRL
BFBBFBFLRR
BFBFFFFLRL
BFFFFBBRRR
BFFBFFBLRR
FBFFFBFLRL
FBFBFBFLRL
FFBBFBFRRR
BFFFFBFRRR
FBBBBBFLRL
BFFFBBBRLL
BFFBBBBLRR
FFBBBBFRLR
BFFFBBFRLR
FBBFFBFLLR
FBFBBBFLRR
FBFFFFBRRR
FFBBBBBLLR
FFBBFFFRRL
FBBFFBBLRL
FBFBBBFRRL
BFFBFBFRRR
FFBBBBFLLR
FFBBFFBLRL
FFBBBBBRLL
FFFBFBBLRL
BFFFBFFLRR
BFBBBFFLRR
FFBFFFFRRR
FBBFFBBLLR
FBBBBFFRRR
BFBBBFFRRL
FBBFFBBLLL
FBFBFBBLRL
BFBBBFFLLR
BBFFFBBLRL
FBBBFBBLLR
BBFFBFFLLL
FBBBFFFRRR
BFFBBFFLRR
FFBBFFFRLL
BFBBFFFLRR
FFBFFFFLLR
FFFBFFBLLL
FFBBBFFRLR
FFBFFFBRRR
FBFBBBBLRL
FBBFBBBRLL
FBBFBFFLLR
FFFFBFBLRR
BFFFBBFLRL
FBFFBBFRLR
BBFFFFBRRR
FFFBBBFLRL
FBBFBFFRRR
BFFBBFBRRR
FFFFBBBRLR
FBBBFBBRLL
FBBFBFFRRL
FBFFFFBLRR
BFFBBBBLRL
FBBBBBFRLR
FFFBFFBLLR
FBBFBFBRLR
FBBBBBFRRR
BFBBFFBRLR
BFFFFFBRRR
FFFBFFBRRR
BFBBBBFLLL
BFBFFFFLRR
FFBBFBBRRR
BBFFFBFRLL
FFBBBBBLRR
FBBBFBFLLR
FBFFFFFRLL
FFBBFFBLRR
FBFFFFFLRR
BFBBFBFRRR
FFBBFFBRLR
FBBFFFBLLL
BFFBFBFLLR
FBBFBFFRLL
FBBBBFBLRL
BFFFFBFRRL
FBFBBFBRRL
BFFFFBBLLL
FBFFBFBLLR
BFFBBFBRLL
BFBFFFBRRL
FBFFBFFLLR
BFBFFFFRRL
FFBFFFBRLR
FFBBBBFLRR
BBFFFFBLLL
BFBBBBBRLL
FFBFBBFRLR
BBFFFFFRLR
FBFFFBBRRR
BFFFBFBRLL
FBBBBFFLRL
BFFFFBFLRR
FBBFBFFLRL
BFBFBFBLRL
FBBFFBFRLR
FBBFFFBLLR
FBBBBFFRLL
BFBBBFFRRR
FBBFBBFLLR
FBBFFBFLRL
BFFBFBBLLR
FBBBFBFLLL
FBBBBBBRRR
FBFBBFBRLR
FFBFBFBRRL
FBFBBBBRRR
FFBBBFBLRR
FBFFBFBLRL
FFBFFFBLRL
BFBFBFFLRR
FBFFFFBLRL
BFFBFFFLRR
BFBBBBFRLL
FBFFBBBLRL
FBFBFBBLRR
BFBFFFBLRL
BFBFBBBLRL
FFBFBFBLRL
BFFBFFBRRL
BBFFFBFRRR
FFFBFFFRLR
FFFBFBFRRL
FFBBBFFLRR
BFBBBFFRLL
BFBBFBBLLL
FBBBBFBLLL
BFFFBFFRLR
BFFBBFBLLL
FFBBFBFLLL
FFFBFBFLLR
FBFFBFFLRR
BFBFFBFRLR
BFFBBBFLLL
FFBFFFBLLL
FFFBFFFRRL
FFBFFFBLRR
FBBFBBFRRR
BBFFFBBLLR
BFFFBFFLLR
FFBFBBBRLL
BFFFBBBLRR
FFBFBFFLLL
FFBFFBBLLL
BFBBFBBRRL
BBFFFFFRRL
FBFFBFFLLL
FFBFFBFLRR
BBFFFFFRRR
FBBFFFBRRL
FBFFBBFLRL
BFFBBBFRRL
BFBBFFFRRL
BFBFFBFLRR
FBBBFFFLLR
FFFFBBBLLR
BFFBFFBLRL
FFBFFFBLLR
FFFBFBBRLL
FBFBBBFLLL
BFBFBFBRRL
BFFFBBBRRL
FFFFBBFRRR
FBBFBBBLRL
FFBBBBBLLL
BBFFBFFLLR
FBFFBBBLLR
BFBFFBFRLL
BFFFFFBLRL
FFFFBFBLLL
FBBBBFBRRL
FBFBFFBLRR
FFFBBFFLLR
FBFBFBFLRR
BBFFFBBLRR
FFFBBFBLLR
FFBBBFBRRR
FFFBBBFRRR
BFBFBFFLLL
FBBBBBFRRL
BFFBFFBLLR
FFBFBBFLRR
BFFBFBBLRR
FBBBFBBLRL
FBFFBBFRLL
BFFBBBBRRL
BFFBBBBRRR
BFFFBBFRLL
BFBBBBBLRR
FFBBBBFLRL
FBBBBFFLRR
BFBFFBBRLR
FBBFBBBLRR
FBFBFBBRRR
BBFFFBBRLL
FBBBBFBRLL
FFBFBFFLLR
FBFFFBFRRR
BFBFBBFRRR
BFFFBFFRRL
BFBFFBFLLR
FFFBBBBLLR
FBBBFFFLRL
FBBFBBFRRL
FBBFBBBLLR
BFFFFBBLLR
FBBBBBBLLL
BFFFFFFRRR
FFFBBBBRLR
FFFBFBFRLR
FFFFBFBLRL
FBFBFFBRRR
FBBBBBBLRR
BFBBBFBRLR
FBFBBBFRLL
FBBFFBBLRR
BFFFBBFRRL
FBBBBFFRLR
BFFBFFBRRR
BFFFBFBLLR
BFFFBBBRRR
BFFBBBFLRL
BFBBFBBLRL
BFFBBFFLLR
BFFFFFBRLR
FBBFFBBRRL
BFFFFFBRRL
FBBBFFBLRL
FBFBBFBRLL
BFFBFBFLLL
BFFBFBBRLR
BFFBFFFLRL
BFBFBBBLLR
FBFBFFBRLL
BFFBBFBLLR
BFFBFBBLLL
BFFBBFBLRL
FBBFFBFRRL
BFBFBBFRLR
FBFFFFBRRL
FBFBFFFRRR
FFFBBFFRRL
FFFFBFBRRL
BFFFFFFLLR
FBBFFFFRLR
FBFBBFFRLR
FFBBFFBRRL
FBBFBBFRLR
FFBBFBFLRL
FFFFBBBLLL
FFBBFFFLLR
BFBBFBBRLL
BFFFFBBRRL
BFFBBFBRRL
FBBFBBBRRL
BFBFBFFLRL
FBFFFBBLRL
FFFFBBBRRR
FBFFBBFLLR
BFFBBFBRLR
FBBFBBFLRL
FFBBFFFRLR
BBFFFBBRRR
FFBBBBBLRL
FBBBBBBRLL
FFFBBBFRLR
FFBBFBFRRL
FFBBBBBRRL
BFBFBBFRLL
FBFFBFFRLR
BFBFBBBRLR
FFBFFFFLRL
FBFFBFBLRR
FBFFBFBRRR
FFFBBFBRRR
FBFFFBFLLL
BFFBFBFRLL
FBFFBFBRLL
FFBFFBBLRR
FFFFBFBRLR
BFFBBBBRLL
BFBBFFBLRR
FFBFFBFLLL
FFBFBBBRLR
FFBFFFFRLR
FBBFFFBRLR
BFFFFFFLLL
BFBBBFFLRL
FBBFBFFLLL
BFBBFBBRRR
BFBFFBBRLL
FBBFBFBLRL
BBFFFFFLLL
FBFFFBFRRL
BFBBBFBLLR
BFFFFBBRLL
FFBFBBFLRL
FFFBFBBLLR
FBFBFFFLRR
FBBBBBBLLR
BFFBFFBRLL
FBFFBFFRRL
FFBFBBBLLR
FBBBFBFLRR
FFBFBBBRRL
FBBFFBBRLR
BFFFBBBLRL
FBBFBBBRRR
BFFBBBFLRR
FBBFFFBRRR
BFBFFFFRLL
BFBBBBBRRR
FBFBBFFRRR
FBBBBBFLRR
FBBBFFBLRR
FFBBBBBRRR
FFFBFFFLLR
BFBBBBFRRR
BFFBFBFLRR
BFFFBBFLLR
FBFFFFFLLL
FBBFFFFRLL
BFFBBBFRLR
BBFFFFBLLR
FBBBBFFLLR
BFFFBFBRLR
BBFFFFFLRL
BFFFFBFLRL
BFFFFBBLRL
FBFFBBBLRR
FBFFBBBRRR
FBFBBFBLRR
FBBBBBBRRL
FFFBFFBLRL
FBFBFBFRLR
FFFBBFBLRR
BFBFFBFLRL
BFBFFFBRLL
BFFFBFBRRR
FBFBBBFLLR
BFFBBBFRRR
BFBFBBFLRR
FBBFBFBLLL
FBFBBBFRRR
BFBBBBFRLR
FFFBBBBLRL
FFFBFFFLLL
FFFBBBFLLL
BFBBFFBRRL
BFBBFBBLLR
FFBBBBFRLL
FBBBBFFRRL
FFBBBFBRRL
FBBFFFBLRL
FFBFFBBRLR
BFBFFBBLLL
FBFFFBFLRR
FFBBFFBLLL
BFFFFBFLLR
FFFBFBFLRL
FFFBBBBRLL
BBFFFBBRRL
BFBFFBBLRR
FFFFBFBLLR
BFBBFBFLLR
BFBBFBFRRL
FFBBFBBLLR
FBFFBBFRRL
BFFBBFFRRL
FBFBBBBLLR
FBFBBBFRLR
BFBFFFFLLL
FFBBFFBLLR
FBFFBBFRRR
BFFFFFFRLL
FBFFFFFLLR
FFFBFFBRRL
FFBBFBBLRL
FBBFBFBLLR
BBFFFBFRRL
FFBBFBFLRR
BFBBFBFLRL
FBFBBBFLRL
BFFFFFFLRL
FFFBFBBRLR
FFBBFBBRLR
FBBFFBFLLL
BFFBFBBLRL
FBFFBBBLLL
FBBBFFFLRR
BFFBBBBLLL
FBBBFBFRLL
FBBBFBBLRR
FBFFFBBRLL
FFBFBBBLRR
FBFBFFFLRL
BFFBFFFRLR
FFBBBFBRLR
FFFBBFBRLL
BFFFFFFLRR
FBBBFBBRRR
FBFFBFFLRL
FBFFBFBLLL
FBBBFBFRLR
FBFBFBBRLL
FBBBFBBLLL
FFBBBFBRLL
FFFBFBFLLL
FBFFFBBRRL
BFFFBFFLLL
FBBFBFBLRR
FBBBBFBLRR
FBBFFBFLRR
FBBBBBBLRL
BFFBFFFRLL
BFBFBBFRRL
BFBFFFFRRR
BFFFBFBRRL
FFFFBFBRLL
FBFBBFFLRR
BBFFFBFLLL
BFBBFFBRRR
FBBFBFBRRR
FBFFBFFRLL
BFBFBBBLRR
FBBFFBFRRR
FBBFBFBRLL
BFFFFBBRLR
BFBFBBBLLL
FBFBFBFLLL
BFFBFFBRLR
BFBFFFBLLR
FFFBFFFRLL
FBFFFFFRRR
FFFBFFFLRR
FFBFFBFRRR
BFFFFBFLLL
FBBBBFBRRR
FBBBFFFLLL
FFBFFBBLLR
BFFFFFFRRL
FFFFBBBLRL
FBFBFBBRLR
FBBBFFBRLR
FBBFBFFRLR
BBFFFBFRLR
FBBFBBFLLL
FBBFFFFLRR
FBFFFBBLLL
BFBBFFFRLL
FFFBFBFRLL
BFFFBBFRRR
FFBFFBBRRL
BBFFFBBLLL
BBFFFFFLLR
BBFFFFBRLL
FBBBFFBRLL
FBFBFBFRRL
FFFBFBBLLL
BFFBFBFLRL
BFBFFBBRRR
FFFBBBBRRL
BFFFBBFLLL
FBFFBBBRLL
FFFBFBBLRR
FBBFFFBLRR
BFBBFFFLLR
FFBBFFFLRL
FBBBFFBRRR
FFFBBFFRLR
FBFFFFBLLR
BFFBFFFRRL
FBFBFBFRRR
FBBBBBFRLL
BFFFFFBRLL
FFFBBFBLRL
BFFFFFBLLL
BFFFBFBLLL
FBFBFFFRLR
BFBFFFFRLR
FBFBBFFRRL
BFBBFFFRLR
FFBFFFFRLL
FFFBBFBRRL
FBBBFFBLLL
BFBFBFBLRR
BFFFFBFRLL
BFBBFFBLLL
FBBFBBBLLL
FBBFBBBRLR
BBFFFFBRRL
BFBFBFFRRL
FBBBFBBRRL
BFBBBBFLRR
FFBFBBBRRR
FFFBFFFLRL
FFFBFFFRRR
FFBBFBBRRL
FFBFBFBLLR
BFBFFFBLLL
FBFBFFBLLL
BFFFBFBLRR
BFFBFFBLLL
BBFFFFBLRR
FFBFBFFRLR
FBFFFBFRLR
FFBBBBBRLR
FBFFFBFRLL
FBFBBBBRLL
FFBFFFBRRL
BFFFBBBLLL
FFBBBFBLLL
BFFFBFFRRR
FFFBBFFRLL
FFFBBBFRRL
FBFBBFFLRL
FFBBFFFLRR
FFFFBBBRRL
FFBBBBFLLL
FFBFFFBRLL
FBFFBBBRRL
BFBBFFFRRR
FFBBBFFLLR
FFBBBFFRRL
BFBBFBFRLR
FFFFBBFLLL
FFBBBBFRRL
FBBFFFFLLL
BFFFBBBRLR
FBFFBBBRLR
BFBBFFFLRL
BFBFBBFLLL
FBFFFFBRLR
BFFBBFFRRR
FBFBBBBLLL
BFFBFBBRLL
FBFBFFBRLR
BFBFBFFLLR
FFFFBBFRLL
BFFBFFFRRR
FBFBBBBRLR
BFBBBBFLRL
BFBFBFBLLL
BFBFFBBLRL
BFBFFBBLLR
BFBBFFBRLL
FFBFBBBLLL
BFBFBBBRLL
BFBFBBBRRR
FFFFBBBLRR
FFFBFBFLRR
BFFFBBBLLR
FBBBBBFLLL
FFFBBFBLLL
FBFBFFFRLL
FBBBFFFRLR
FFBFBFFLRR
FFFFBBFRLR
FFFFBFBRRR
FFFBBFBRLR
FFBFBFBLLL
FFBFFFFLRR
FFFBFBFRRR
FFBBFFFLLL
FBBBFFBLLR
BFBFBBBRRL
FFBBBFBLRL
BFBBBBBRRL
FFFBBBBLRR
FBBBFFBRRL
FFBFBFFRRL
FBBBBBBRLR
FBFFBFFRRR
BFFFFBFRLR
FFBBFFBRLL
BFFBBBFLLR
FBFBFBFRLL
BFBFBFBRLR
FBFFFBBLLR
FBFBFFBRRL
FBBFFFBRLL
FFBFBFBRLR
FFBFBFFRLL
FFFBFFBRLR
BFBFBFBRRR
FFFBBBBRRR
BFBFFBFRRR
BFBBFFBLRL
FBBFFBFRLL
BFFBBFFLRL
FFBFBFBRLL
FBFBBBBLRR
BFBFBFBRLL
BFBFFBFRRL
BFFFFFFRLR
FFBFFBBRRR
FFBBFBFLLR
FFFBBFFLLL
BFBBBFBLRL
FBFFFFBRLL
FBBBFBBRLR
BFFFBBFLRR
FBBBBFBRLR
BFBBBFFLLL
FBFBFBBLLL
BBFFFFBRLR
FBFBFFFLLR
FBFBBBBRRL
FFBFBBFRRL
BFFBBFFLLL
FBBFBBFLRR
BFFFFFBLLR
BFBBFFFLLL
FBBFBFFLRR
FBBFFBBRRR
FBFFFFFLRL
BFBFFFBLRR
FFFBFFBLRR
FBBFFBBRLL
BFBBBBBLRL
FFFBBBFLRR
BFBBBFBLLL
FBFFFBBRLR
FFBBFBBRLL
FBFFFBBLRR
FBFBBFFLLR
FFFFBBFRRL
FBBFFFFRRR
BFFBFFFLLR
FFFBBFFLRL
FFFBBBFLLR
BFFFBFFLRL
FBBBBFBLLR
FFBFBFBLRR
BFBBFBFLLL
BFFBBFFRLR
BFBBBBFLLR
FFFFBBFLRR
BFBFBBFLRL
BBFFFBFLRR
BFBBFBBRLR
FBFBFFBLRL
FFFBBFFLRR
FFBBFFFRRR
BFFBBBBLLR
BBFFFFBLRL
FBFFBBFLLL
FFFFBBFLLR
FBBBFBFRRL
FFBFFBBLRL
BFBBFFBLLR
BFBFFFFLLR
BFBBBBBRLR
BFBBFBFRLL
BFFBFFFLLL
FFBFFFFLLL
BFBFFBFLLL
FBBFFFFLRL
BFBBBBBLLR
BFFBBFBLRR
BFFFBFBLRL
FBBBFFFRLL
FBBFBFBRRL
FBFFFFFRRL'''

def solve(cases):
    highest = 0
    result = None
    cases = cases.split('\n')
    for case in cases:
        sit = seat(case)
        if sit[2] > highest:
            highest = sit[2]
            result = sit
    return highest, result

def seat(case):
    rows = case[:7]
    columns = case[7:]
    row = calc_rows(rows)
    column = calc_columns(columns)
    seat_id = 44 * row + columns
    return (row, column, seat_id)

def calc_rows(rows):
    print(rows)
    min = 0
    max = 127
    for char in rows:
        if char == 'F':
            max = min + math.floor((max - min) / 2)
        elif char == 'B':
            min = min + math.ceil((max - min) / 2)
    return min, max

def calc_columns(columns):
    pass

if __name__ == '__main__':
    t = calc_rows('F')
    if t != (0, 63):
        print('F failed', t)
        exit()
    t = calc_rows('FB')
    if t != (32, 63):
        print('B failed', t)
        exit()

    for test in TESTS:
        test_result = solve(test)
        if test_result != TESTS[test]:
            print(test, test_result, TESTS[test])
            exit()

    test_results = solve(INPUT)
    print('results', test_results)
    if test_results != TEST_RESULT:
        exit()
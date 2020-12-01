import sys

TESTS = {
  '(())': 0,
  '()()': 0,
  ')(()': 0,
  '(((': 3,
  '(()(()(': 3,
  '))(((((': 3,
  '())': -1,
  '))(': -1,
  ')()': -1,
  ')))': -3,
  ')())())': -3,
}

def test():
  results = {
    'success': 0,
    'failure': []
  }
  for case in TESTS:
    result, expected = solve(case), TESTS[case]
    if result == TESTS[case]:
      results['success'] += 1
      continue
    results['failure'].append((case, expected, result))

  return results

def solve(input=''):
  floor = 0
  for char in input:
    if char == '(':
      floor += 1
      continue
    floor -= 1 # Yes, I know other characters could sneak in and break things.
  return floor

if __name__ == '__main__':
  argv = sys.argv[1:]
  print(argv)

  if argv and argv[0].lower() == 'test':
    print(test())
  
  print(solve())
  
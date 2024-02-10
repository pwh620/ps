# https://www.acmicpc.net/problem/1004
import sys

def input_integers() -> tuple[int]:
  return tuple([int(x) for x in sys.stdin.readline().rstrip().split(' ')])

def log(x):
  # import inspect
  # line_number = inspect.currentframe().f_back.f_lineno
  # print(f"[{line_number}] {x}")
  pass

SMALL_ENOUGH = -10000000
C, = input_integers()

def check_possible_adjacent_lines(line1, line2):
  return ((line1 * 2) & line2) == 0 and (line1 & (line2 * 2)) == 0

def check_valid_line(line):
  previous_bit = 0
  while line:
    current_bit = line & 1
    if previous_bit == 1 and current_bit == 1:
      return False
    line >>= 1
    previous_bit = current_bit
  return True

def check_broken_position(line, broken):
  return line & broken == 0

def check_line(line, broken):
  return check_broken_position(line, broken) and check_valid_line(line)

def number_of_1(x):
  count = 0
  while x:
    count += x & 1
    x >>= 1
  return count

for _ in range(C):
  N, M = input_integers()
  broken_positions = [
    sum([2 ** i if broken == 'x' else 0 for i, broken in enumerate(sys.stdin.readline().rstrip())])
    for _ in range(N)
  ]

  possible_adjacent_line_matrix = [
    [j for j in range(2 ** M) if check_possible_adjacent_lines(i, j)]
    for i in range(2 ** M)
  ]
  log(possible_adjacent_line_matrix)

  # first line
  current_line_students = [
    number_of_1(line) if check_line(line, broken_positions[0]) else SMALL_ENOUGH
    for line in range(2 ** M)
  ]
  log(current_line_students)

  previous_line_students = current_line_students
  for line_number in range(1, N):
    current_line_students = []

    for line in range(2 ** M):
      if check_line(line, broken_positions[line_number]):
        candidates = [
          previous_line_students[possible_previous_line] + number_of_1(line)
          for possible_previous_line in possible_adjacent_line_matrix[line]
        ]
        log(candidates)
        current_line_students.append(max(candidates) if candidates else SMALL_ENOUGH)
      else:
        current_line_students.append(SMALL_ENOUGH)
    previous_line_students = current_line_students
  print(max(previous_line_students))
# https://www.acmicpc.net/problem/1040

from functools import lru_cache

def count_bits(n):
  count = 0
  while n:
    count += n & 1
    n >>= 1
  return count

@lru_cache(maxsize=None)
def find_smallest_with(k, used_digits_in_bitmask, number_of_remain_digits):
  if count_bits(used_digits_in_bitmask) + number_of_remain_digits < k:
    return 
  if number_of_remain_digits == 0:
    if count_bits(used_digits_in_bitmask) != k:
      return 
    return ""
  for i in range(10):
    if i == 0 and used_digits_in_bitmask == 0:
      continue
    result = find_smallest_with(k, used_digits_in_bitmask | (1 << i), number_of_remain_digits - 1)
    if result is not None:
      # return i * (10 ** (number_of_remain_digits - 1)) + result
      return str(i) + result
  return   

def make_used_digits_in_bitmask(n):
  bitmask = 0
  for c in n:
    bitmask |= 1 << int(c)
  return bitmask

def log(x):
  import inspect
  line_number = inspect.currentframe().f_back.f_lineno
  # print(f"[{line_number}] {x}")
  pass


def find_smallest_above(k, n):
  number_of_last_digit = 0
  # digit_length = len(str(n))
  heading_digits = str(n)
  while number_of_last_digit <= 25:
    result = find_smallest_with(k, make_used_digits_in_bitmask(heading_digits), number_of_last_digit)
    log(f"{n}, {heading_digits}, {number_of_last_digit}, {count_bits(make_used_digits_in_bitmask(heading_digits))} {result}")
    if result is not None:
      return heading_digits + str(result)
    if heading_digits[-1] == '9':
      if len(heading_digits) > 1:
        # heading_digits = heading_digits[:-1]
        heading_digits = str(int(heading_digits) + 1)[:-1]
        # heading_digits = heading_digits[:-1] + str(int(heading_digits[-1]) + 1)
      else:
        heading_digits = "1"
      number_of_last_digit += 1
    else:
      heading_digits = heading_digits[:-1] + str(int(heading_digits[-1]) + 1)
  return 

def assertion(n, k, answer):
  result = find_smallest_above(k, n)
  assert result == str(answer), (k, n, result, answer)

import sys
def input_integers() -> tuple[int]:
  return tuple([int(x) for x in sys.stdin.readline().rstrip().split(' ')])

# assertion(47, 1, 55)
# assertion(12364, 3, 12411)
# assertion(7, 3, 102)
# assertion(69, 2, 69)
n, k = input_integers()
result = find_smallest_above(k, n)
print(result)


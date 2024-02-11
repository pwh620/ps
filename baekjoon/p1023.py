# https://www.acmicpc.net/problem/1023

from functools import lru_cache

@lru_cache(maxsize=None)
def number_of_valid(remain, opened):
  if remain < opened:
    return 0
  if opened < 0:
    return 0
  if remain == 1:
    if opened == 1:
      return 1
    else:
      return 0
  else:
    return number_of_valid(remain - 1, opened - 1) + number_of_valid(remain - 1, opened + 1)

def is_valid_head(head):
  opened = 0
  for c in head:
    if c == '(':
      opened += 1
    else:
      opened -= 1
    if opened < 0:
      return -1
  return opened

def number_of_invalid(head, length):
  remain = length - len(head)
  opened = is_valid_head(head)
  if opened < 0:
    return 2 ** remain
  return 2 ** remain - number_of_valid(remain, opened)

def go(n, k):
  head = ""
  k = k + 1
  kk = 0
  while len(head) < n:
    number_if_open = number_of_invalid(head + "(", n)
    if k > kk + number_if_open:
      head += ")"
      kk += number_if_open
      continue
    elif k <= kk + number_if_open:
      head += "("
      continue
  if k - 1 == kk:
    return head
  else:
    return -1

import sys
def input_integers() -> tuple[int]:
  return tuple([int(x) for x in sys.stdin.readline().rstrip().split(' ')])

n, k = input_integers()
print(go(n, k))
# for i in range(65):
#   result = go(6, i)
#   print(i, result)
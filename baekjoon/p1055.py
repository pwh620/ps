# https://www.acmicpc.net/problem/1055

def search(S, remain_depth, n):
  # print(S, remain_depth, n)
  result = remain_depth, n
  while isinstance(result, tuple):
    remain_depth, n = result
    result = '-'
    if remain_depth == 0:
      if len(input_string) <= n:
        result = '-'
      else:
        result = input_string[n] 
    else:
      index = 0
      for c in S:
        if c == '$':
          if index <= n < index + sizes[remain_depth - 1]:
            result = (remain_depth - 1, n - index)
            break
          else:
            index += sizes[remain_depth - 1]
        else:
          if n == index:
            result = c
            break
          else:
            index += 1
  return result

def input_integers() -> tuple[int]:
  import sys
  return tuple([int(x) for x in sys.stdin.readline().rstrip().split(' ')])

input_string = input()
S = input()
n, = input_integers()
min_index, max_index = input_integers()

number_of_end = S.count('$')

result = ""
if number_of_end == 1:
  for index in range(min_index, max_index + 1):
    if index <= len(input_string):
      result += input_string[index - 1]
    elif index <= len(input_string) + (len(S) - 1) * n:
      result += S[(index - len(input_string) - 1) % (len(S) - 1) + 1]
    else:
      result += '-'
else:
  sizes = [len(input_string)]
  for i in range(n):
    size = sizes[-1] * number_of_end + (len(S) - number_of_end)
    if size > max_index:
      break
    sizes.append(size)
  n = min(n, len(sizes))
  for index in range(min_index, max_index + 1):
    result += search(S, n, index - 1)
print(result)
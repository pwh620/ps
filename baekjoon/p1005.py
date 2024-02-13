import sys

def input_integers() -> tuple[int]:
  return tuple([int(x) for x in sys.stdin.readline().rstrip().split(' ')])

def go(w, dependancies_map, time_map, ds):
  building_number_stack = [w]
  while building_number_stack:
    building_number = building_number_stack.pop()
    if building_number in time_map:
      continue
    building_number_stack.append(building_number)

    dep_time = 0
    if building_number in dependancies_map and dependancies_map[building_number]:
      added = False
      for dep in dependancies_map[building_number]:
        if dep not in time_map:
          building_number_stack.append(dep)
          added = True
        else:
          dep_time = max(dep_time, time_map[dep])
      if added:
        continue

    time_map[building_number] = dep_time + ds[building_number]
    building_number_stack.pop()
  return time_map[w]

T, = input_integers()
for _ in range(T):
  N, K = input_integers()
  Ds = input_integers()

  ds = {i: Ds[i-1] for i in range(1, N + 1)}

  dependancies_map = {i: [] for i in range(1, N + 1)}

  time_map = {}

  for k in range(K):
    x, y = input_integers()
    dependancies_map[y].append(x)

  w = int(sys.stdin.readline().rstrip())

  print(go(w, dependancies_map, time_map, ds))
  # print(ds)
  # print(dependancies_map)
  # print(time_map)
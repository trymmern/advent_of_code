f = open("input.txt", "r")

arr = []
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for l in f:
  arr.append([x for x in l.strip()])

def check_adjacent(i, j):
  count = 0
  for d in directions:
    if i + d[0] < 0 or i + d[0] >= len(arr) or j + d[1] < 0 or j + d[1] >= len(arr[0]):
      continue

    if arr[i + d[0]][j + d[1]] == '@':
      count += 1

  return count < 4

total_can_move = 0

for (i, row) in enumerate(arr):
  for (j, val) in enumerate(row):
    can_move = False
    if val == '@':
      total_can_move += 1 if check_adjacent(i, j) else 0
    else:
      continue


print(total_can_move)
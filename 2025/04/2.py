f = open("input.txt", "r")

arr = []
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for l in f:
  arr.append([x for x in l.strip()])

def can_remove(grid, i, j):
  count = 0
  for d in directions:
    ni, nj = i + d[0], j + d[1]
    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
      if grid[ni][nj] == '@':
        count += 1
  return count < 4

total_removed = 0
removed_this_round = True

while removed_this_round:
  removed_this_round = False

  to_remove = []
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] == '@' and can_remove(arr, i, j):
        to_remove.append((i, j))

  for i, j in to_remove:
    arr[i][j] = '.'
    total_removed += 1
    removed_this_round = True

print(total_removed)
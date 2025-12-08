f = open("input.txt", "r")

def parse_input(file):
  lines = []
  for line in file:
    lines.append([x for x in line.strip()])

  return lines

grid = parse_input(f)
f.close()

def count_timelines(grid, r, c, memo=None):
  if r == len(grid) - 1:
    return 1
  
  if memo and (r, c) in memo:
    return memo[(r, c)]
  
  next_row = r + 1
  next_cell = grid[next_row][c]

  if next_cell == "." or next_cell == "|":
    res = count_timelines(grid, next_row, c, memo)
  elif next_cell == "^":
    left_res = count_timelines(grid, next_row, c - 1, memo)
    right_res = count_timelines(grid, next_row, c + 1, memo)
    res = left_res + right_res

  if memo is not None:
    memo[(r, c)] = res

  return res

start = (0, 0)
for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == 'S':
      start = (r, c)
      break

memo = {}
total_timelines = count_timelines(grid, start[0], start[1], memo)

print("Total distinct timelines:", total_timelines)
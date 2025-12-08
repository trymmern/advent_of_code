f = open("input.txt", "r")

def parse_input(file):
  lines = []
  for line in file:
    lines.append([x for x in line.strip()])

  return lines

def update_grid(row, index):
  new_grid = [row.copy() for row in grid]
  splits = 0
  for c in range(len(row)):
    cell = grid[index][c]
    if cell == "S":
      new_grid[index + 1][c] = "|"
    if cell == "^":
      if grid[index - 1][c] == "|":
        splits += 1
        new_grid[index][c - 1] = "|"
        new_grid[index][c + 1] = "|"
    if cell == ".":
      if grid[index - 1][c] == "|":
        new_grid[index][c] = "|"
  return new_grid, splits

grid = parse_input(f)
splits = 0
index = 0
print(grid)
while index < len(grid) - 1:
  new_grid, new_splits = update_grid(grid[index], index)
  grid = new_grid
  splits += new_splits
  print("New splits this round:", new_splits)
  index += 1

for row in grid:
  print("".join(row))

print("Total splits:", splits)
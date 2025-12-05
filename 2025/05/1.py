f = open("input.txt", "r")

def parse_input(file):
  ranges, ingredients = [], []
  ranges_done = False
  for line in file:
    if line.strip() == "":
      ranges_done = True
      continue
    if not ranges_done:
      r = line.strip().split("-")
      ranges.append((int(r[0]), int(r[1])))
    else:
      ingredients.append(int(line.strip()))
  return ranges, ingredients

ranges, ingredients = parse_input(f)

count = 0
for i in ingredients:
  in_range = any(r[0] <= i <= r[1] for r in ranges)
  count += 1 if in_range else 0

print("Total valid ingredients:", count)
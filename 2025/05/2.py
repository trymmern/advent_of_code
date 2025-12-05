f = open("input.txt", "r")

def parse_input(file):
  data = []
  for line in file:
    if line.strip() == "":
      return data
    r = line.strip().split("-")
    data.append((int(r[0]), int(r[1])))
  return data

data = parse_input(f)
data.sort()
merged_intervals = []
for start, end in data:
  if not merged_intervals or merged_intervals[-1][1] < start - 1:
    merged_intervals.append([start, end])
  else:
    merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

count = 0
for start, end in merged_intervals:
  count += end - start + 1

print("Count:", count)
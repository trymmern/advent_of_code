f = open("input.txt", "r")

arr = list(range(0, 100))
index = 50
count = 0

for l in f:
  direction, n = l.strip()[0], int(l.strip()[1:])

  old_index = index

  if direction == "R":
    first_hit = len(arr) - old_index
    if first_hit <= n:
      count += 1 + (n - first_hit) // len(arr)

    index = (index + n) % len(arr)

  elif direction == "L":
    first_hit = old_index
    if first_hit == 0:
      first_hit = len(arr)

    if first_hit <= n:
      count += 1 + (n - first_hit) // len(arr)

    index = (index - n) % len(arr)
      
print(count)
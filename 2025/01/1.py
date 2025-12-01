f = open("input.txt", "r")

arr = list(range(0, 100))
index = 50
count = 0

for l in f:
  direction, n = l.strip()[0], int(l.strip()[1:])

  if direction == "R":
    index = (index + n) % len(arr)
  elif direction == "L":
    index = (index - n) % len(arr)

  if (index == 0):
    count += 1

print(count)
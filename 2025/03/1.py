f = open("input.txt", "r")

count = 0
for l in f:
  batteries = list(map(int, l.strip()))
  print(batteries)
  length = len(batteries)

  a = max(batteries)
  index = batteries.index(a)
  if index == length - 1:
    a = max(batteries[:index])
    index = batteries.index(a)

  b = max(batteries[index+1:])

  count += int(str(a) + str(b))

print(count)
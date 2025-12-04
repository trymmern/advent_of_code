f = open("input.txt", "r")

def get_max_joltage(batteries, keep_count=12):
  remove_count = len(batteries) - keep_count
  stack = []

  for digit in batteries:
    while stack and remove_count > 0 and stack[-1] < digit:
      stack.pop()
      remove_count -= 1
    stack.append(digit)

  while remove_count > 0:
    stack.pop()
    remove_count -= 1

  return int(''.join(map(str, stack)))

total = 0
for line in f:
  batteries = list(map(int, line.strip()))
  joltage = get_max_joltage(batteries, 12)
  total += joltage

print(total)
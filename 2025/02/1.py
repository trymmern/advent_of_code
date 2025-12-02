f = open("input.txt", "r")

arr = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

def has_repeating_pattern(n):
  s = str(n)
  length = len(s)
  if length % 2 != 0:
    return False
  mid = length // 2
  return s[:mid] == s[mid:]

total_sum = 0
for start, end in arr:
  for n in range(start, end + 1):
    if has_repeating_pattern(n):
      total_sum += n

print(total_sum)
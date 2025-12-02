f = open("input.txt", "r")

arr = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

def has_repeating_pattern(n):
  s = str(n)
  length = len(s)
  for pattern_len in range(1, length // 2 + 1):
    if length % pattern_len == 0:
      pattern = s[:pattern_len]
      repetitions = length // pattern_len
      if repetitions >= 2 and pattern * repetitions == s:
        return True
  return False

total_sum = 0
for start, end in arr:
  for n in range(start, end + 1):
    if has_repeating_pattern(n):
      total_sum += n

print(total_sum)
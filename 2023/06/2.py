import numpy as np

f = open("input.txt", "r").read().strip()

t, d = f.strip().split('\n')
t = int(str.replace(t.split(':')[1], ' ', ''))
d = int(str.replace(d.split(':')[1], ' ', ''))
print(t, d)

total = 0
for ms in range(t):
    D = ms * (t - ms)
    if D > d:
        total += 1

print(total)
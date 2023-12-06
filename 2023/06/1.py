import numpy as np

f = open("input.txt", "r").read().strip()

t, d = f.strip().split('\n')
t = [int(x) for x in t.split(':')[1].split()]
d = [int(x) for x in d.split(':')[1].split()]
print(t, d)

games = []
for i in range(len(t)):
    games.append((t[i], d[i]))

S = []
for g in games:
    count = 0
    t, d = g
    print(f'Game with t = {t}, d = {d}')
    for ms in range(t):
        D = ms * (t - ms)
        if D > d:
            count += 1
    S.append(count)
print(np.prod(S))
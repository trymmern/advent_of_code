from itertools import cycle
from math import lcm

D = open("input.txt", "r").read().strip().split('\n')

RL = cycle([x for x in D[0]])

paths = {}
for i in range(2, len(D)):
    parts = D[i].split('=')
    l, r = parts[1].split(',')
    l = l.replace('(', '').strip()
    r = r.replace(')', '').strip()
    paths.update({parts[0].strip(): (l, r)})

def get_curr(nxt, i):
    if nxt == 'L':
        return paths[nodes[i]][0]
    elif nxt == 'R':
        return paths[nodes[i]][1]

nodes = [x for x in paths.keys() if x[-1] == 'A']
count = 0
found = False
results = []
while not found:
    nxt = next(RL)

    count += 1
    for i, c in enumerate(nodes):
        nodes[i] = get_curr(nxt, i)
        if nodes[i][-1] == 'Z':
            results.append(count)
            
    if len(results) == len(nodes):
        found = True

print(lcm(*results))
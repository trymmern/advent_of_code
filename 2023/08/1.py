from itertools import cycle

D = open("input.txt", "r").read().strip().split('\n')

RL = cycle([x for x in D[0]])

paths = {}
for i in range(2, len(D)):
    parts = D[i].split('=')
    l, r = parts[1].split(',')
    l = l.replace('(', '').strip()
    r = r.replace(')', '').strip()
    paths.update({parts[0].strip(): (l, r)})

def get_curr(nxt):
    if nxt == 'L':
        return paths[curr][0]
    elif nxt == 'R':
        return paths[curr][1]

curr = 'AAA'
count = 0
found = False
while found == False:
    nxt = next(RL)
    curr = get_curr(nxt)
    count += 1

    if curr == 'ZZZ':
        found = True

print(count)
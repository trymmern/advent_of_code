from typing import List

f = open("input.txt", "r")

x = 1
cycle = 0
signals: List[int] = []
for l in f:

    cmd = l.strip().split(" ")

    if cmd[0] == 'noop':
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signals.append(cycle*x)
        continue
    else:
        for i in range(2):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signals.append(cycle*x)

        x += int(cmd[1])
    print(cycle, x)
print(signals)
print(sum(signals))
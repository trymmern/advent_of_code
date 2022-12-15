import numpy as np
from matplotlib import pyplot
import re

f = open("input.txt", "r")

Map = {}
def main():
    f.seek(0,0)
    for l in f:
        P = [int(x) for x in re.findall(r'\d+', l.strip())]
        s = P[:2]
        b = P[2:]
        Map[(s[0], s[1])] = 's'
        Map[(b[0], b[1])] = 'b'

        # points = [(int(x[0]), int(x[1])) for x in P]
        
        # for p1, p2 in zip(points, points[1:]):
        #     x1, y1 = p1
        #     x2, y2 = p2

        #     for x in range(min(x1, x2), max(x1, x2) + 1):
        #         Map[(x, y1)] = 1
            
        #     for y in range(min(y1, y2), max(y1, y2) + 1):
        #         Map[(x1, y)] = 1
    print(Map)


def max_y(cave):
    return max(y for (_, y) in cave.keys())

def sand_falling(cave):
    x = 500

    for y in range(max_y(cave)):
        if (x, y + 1) not in cave:
            continue
        elif (x - 1, y + 1) not in cave:
            x -= 1
        elif (x + 1, y + 1) not in cave:
            x += 1
        else:
            cave[(x, y)] = 2
            return (x, y) != (500, 0)
    return False

main()
import numpy as np
from matplotlib import pyplot

f = open("input.txt", "r")

start = (500,0)
cave = {}
def main():
    f.seek(0,0)
    for l in f:
        P = [x.split(",") for x in l.strip().split("->")]
        points = [(int(x[0]), int(x[1])) for x in P]
        
        for p1, p2 in zip(points, points[1:]):
            x1, y1 = p1
            x2, y2 = p2

            for x in range(min(x1, x2), max(x1, x2) + 1):
                cave[(x, y1)] = 1
            
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cave[(x1, y)] = 1

    add_floor(cave)
    
    while sand_falling(cave):
        pass

    sand = sum(v == 2 for v in cave.values())
    print(sand)

def add_floor(cave):
    y = max_y(cave) + 2
    for x in range(-1000, 1001):
        cave[(x, y)] = 1

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
import numpy as np
from matplotlib import pyplot

f = open("input.txt", "r")

start = (500,0)
def main():
    m = fill_matrix()
    # m[start[1], start[0]] = 2
    keep_falling = True
    sand = 0

    while keep_falling:
        # if sand == 200:
        #     keep_falling = False
        if check_sand(m):
            sand += 1
        else:
            keep_falling = False
    
    print(sand)
    
    pyplot.imshow(m)
    # pyplot.colorbar()
    pyplot.show()

def check_sand(m) -> bool:
    final = get_lowest(m, start[0], start[1])
    if final == -1: return False
    else:
        m[final[1]][final[0]] = 2
        return True
        
def get_lowest(m: np.ndarray, x: int, y: int):
    for i in range(y, len(m)):
        if m[i][x] in (1, 2): # Found wall or sand
            if can_move_left(m, x, i-1):
                return get_lowest(m, x-1, i)
            elif can_move_right(m, x, i-1):
                return get_lowest(m, x+1, i)
            else:
                return (x, i-1) # final spot of sand grain
    print("found void")
    return -1

def can_move_left(m: np.ndarray, x: int, y: int):
    return m[y+1][x-1] not in (1, 2)

def can_move_right(m: np.ndarray, x: int, y: int):
    return m[y+1][x+1] not in (1, 2)

def fill_matrix() -> np.ndarray:
    m = np.array([])
    x, y = get_matrix_size()
    print(x, y)
    for _ in range(y+1):
        row = [[0]*(x+1)]
        if len(m) < 1:
            m = np.array(row)
        else:
            m = np.append(m, row, axis=0)
    
    f.seek(0,0)
    for l in f:
        P = [x.split(",") for x in l.strip().split("->")]
        points = [(int(x[0]), int(x[1])) for x in P]
        
        for p1, p2 in zip(points, points[1:]):
            x1, y1 = p1
            x2, y2 = p2

            for x in range(min(x1, x2), max(x1, x2) + 1):
                m[y1][x] = 1
            
            for y in range(min(y1, y2), max(y1, y2) + 1):
                m[y][x1] = 1
    return m

def get_matrix_size():
    x, y = (0, 0)
    for l in f:
        coords = get_coordinates(l)
        for c in coords:
            curr_x = int(c.split(",")[0])
            curr_y = int(c.split(",")[1])
            if curr_x > x:
                x = curr_x
            if curr_y > y:
                y = curr_y
    
    return (x, y)

def get_coordinates(l: str):
    return l.strip().split(" -> ")

main()
import numpy as np
from matplotlib import pyplot

f = open("input.txt", "r")

start = (500,0)
def main():
    m = fill_matrix()
    m[start[1], start[0]] = 2
    keep_falling = True
    sand = 0

    while keep_falling:
        if check_sand(m):
            sand += 1
        else:
            keep_falling = False
    
    print(sand)
    
    pyplot.imshow(m)
    # pyplot.colorbar()
    pyplot.show()

def check_sand(m) -> bool:
    can_move = True
    while can_move:
        max_y = get_lowest(m, start[0], start[1])
        
        if max_y == -1: return False


        
def get_lowest(m: np.ndarray, x: int, y: int):
    for i in range(y, len(m)):
        if i >= len(m): return -1 # Found void
        elif m[i+1][x] == 1: # Found wall
            if can_move_left(x, i):
            elif can_move_right(x, i): 
            ## TODO: check if can move left or right and move and recurse until it cant no mo


def fill_matrix() -> np.ndarray:
    m = np.array([])
    x, y = get_matrix_size()
    for _ in range(y+1):
        row = [[0]*(x+1)]
        if len(m) < 1:
            m = np.array(row)
        else:
            m = np.append(m, row, axis=0)
    
    f.seek(0,0)
    for l in f:
        l = l.strip()
        c = get_coordinates(l)
        for i in range(1, len(c)):
            coords = c[i].split(",")
            x, y = (int(coords[0]), int(coords[1]))
            prev_x, prev_y = (int(c[i-1].split(",")[0]), int(c[i-1].split(",")[1]))

            if prev_x == x: # vertical
                for i in range(prev_y, y):
                    m[i][x] = 1
            elif prev_y == y: # horizontal
                for i in range(prev_x, x):
                    m[y][i] = 1
            m[y][x] = 1
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
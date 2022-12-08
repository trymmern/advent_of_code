import numpy as np
from matplotlib import pyplot as plt

f = open("input.txt", "r")

def main():
    m = fill_matrix()
    score = get_visible(m)
    print(score)


def get_visible(m: np.ndarray) -> int:
    score = 0
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if y == 0 or y == len(m)-1 or x == 0 or x == len(m)-1:
                score += 1
            else:
                if is_visible_vertically(m, x, y) or is_visible_horizontally(m, x, y):
                    score += 1
    return score

def is_visible_vertically(m, x: int, y: int) -> bool:
    visible_top = True
    visible_bot = True
    for i in range(0, y):
        if m[i][x] >= m[y][x]:
            visible_top = False
            break
    
    for i in range(y+1, len(m)):
        if m[i][x] >= m[y][x]:
            visible_bot = False
            break

    return visible_top or visible_bot

def is_visible_horizontally(m, x: int, y: int) -> bool:
    visible_left = True
    visible_right = True
    for i in range(0, x):
        if m[y][i] >= m[y][x]:
            visible_left = False
            break

    for i in range(x+1, len(m[y])):
        if m[y][i] >= m[y][x]:
            visible_right = False
            break
    
    return visible_left or visible_right

def fill_matrix() -> np.ndarray:
    m = np.array([])
    for l in f:
        row = [[int(x) for x in l.strip()]]
        if len(m) < 1:
            m = np.array(row)
        else:
            m = np.append(m, row, axis=0)
    return m

main()
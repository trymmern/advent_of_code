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
            current_score = vertical_score(m, x, y) * horizontal_score(m, x, y)
            if current_score > score:
                score = current_score
    return score

def vertical_score(m, x: int, y: int) -> int:
    score_up = 0
    score_down = 0
    for i in range(y-1, -1, -1):
        if m[i][x] < m[y][x]:
            score_up += 1
        elif m[i][x] >= m[y][x]:
            score_up += 1
            break
    
    for i in range(y+1, len(m)):
        if m[i][x] < m[y][x]:
            score_down += 1
        if m[i][x] >= m[y][x]:
            score_down += 1
            break

    return score_up * score_down

def horizontal_score(m, x: int, y: int) -> bool:
    score_left = 0
    score_right = 0
    for i in range(x-1, -1, -1):
        if m[y][i] < m[y][x]:
            score_left += 1
        elif m[y][i] >= m[y][x]:
            score_left += 1
            break

    for i in range(x+1, len(m[y])):
        if m[y][i] < m[y][x]:
            score_right += 1
        if m[y][i] >= m[y][x]:
            score_right += 1
            break
    
    return score_left * score_right

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
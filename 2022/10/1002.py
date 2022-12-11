from typing import List
import numpy as np

f = open("input.txt", "r")

def main():
    x = 1
    cycle = 0
    y = 0
    pixels = fill_matrix()

    for l in f:
        cmd = l.strip().split(" ")

        if cycle == 40:
            cycle = 0
            y += 1

        if cmd[0] == 'noop':
            draw_pixel(cycle, y, x, pixels)
            cycle += 1
        else:
            for _ in range(2):
                draw_pixel(cycle, y, x, pixels)
                cycle += 1
            x += int(cmd[1])
        print(cycle, x)
    print(pixels)

def draw_pixel(cycle: int, y: int, x: int, pixels: List[List[str]]):
    print(pixels)
    if cycle in [x-1, x, x+1]:
        pixels[y][cycle] = "#"
    else:
        pixels[y][cycle] ="."

def fill_matrix() -> np.ndarray:
    m = np.array([])
    for _ in range(6):
        row = [['.']*40]
        if len(m) < 1:
            m = np.array(row)
        else:
            m = np.append(m, row, axis=0)
    return m

main()
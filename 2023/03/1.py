import numpy as np

f = open("input.txt", "r")

def main():
    m = np.empty((len(f.readline().strip()), len(f.readlines())+1), dtype=str)
    f.seek(0)
    index = 0
    for x in f:
        for jindex in range(len(x.strip())):
            m[index][jindex] = x.strip()[jindex]
        index += 1

    sum = 0
    number = ''
    for i in range(len(m)):
        is_part = False
        for j in range(len(m[i])):
            if is_sign(m[i][j]) or m[i][j] == '.':
                if is_part:
                    sum += int(number)
                number = ''
                is_part = False
                continue
            elif m[i][j].isdigit():
                number += m[i][j]
                adj = adj_cells(m, (j, i))
                if i < 1:
                    print(adj)
                if True in [is_sign(c) for c in adj]:
                    is_part = True
                if j == len(m[i])-1 and is_part:
                    sum += int(number)
                    number = ''
                    is_part = False
    print(sum)

def is_sign(c) -> bool:
    if c.isdigit():
        return False
    if c == '.':
        return False
    return True

def adj_cells(m, position):
    adj = []
    
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, m.shape[0])  # X bounds
            rangeY = range(0, m.shape[1])  # Y bounds
            
            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append(m[newY][newX])
    return adj

main()
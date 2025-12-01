import numpy as np

f = open("input.txt", "r")

M = []
for l in f:
    M.append([int(x) for x in l.strip()])

sum = 0
heads = [(j, i) for i in range(len(M)) for j in range(len(M[i])) if M[i][j] == 0]
for x, y in heads:
    def find_paths(y, x, path):
        if M[y][x] == 9:
            paths.append(path)
            return
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(M) and 0 <= nx < len(M[0]) and M[ny][nx] == M[y][x] + 1:
                find_paths(ny, nx, path + [(ny, nx)])

    paths = []
    find_paths(y, x, [(y, x)])
    print(f"Paths from ({y}, {x}): {paths}")
    sum += len(paths)

print(sum)
m = np.array(M)
print(m)
f = open("input.txt", "r")
lines = f.readlines()
nl = enumerate(lines)

B = [] # Board
V = [] # Visited locations
pos = () # (x, y)
dir = "up"
for i, l in nl:
    print(i, l)
    for j, c in enumerate(l.strip()):
        if c != "." and c != "#":
            print(j, i, c)
            pos = (j, i)
            V.append(pos)
    B.append([c for c in l.strip()])

x = len(B[0])
y = len(B)

inside = True
while inside:
    if dir == "up":
        if pos[1]-1 < 0:
            inside = False
            continue
        if B[pos[1]-1][pos[0]] == "#":
            dir = "right"
            continue
        else:
            pos = (pos[0], pos[1]-1)
            if pos not in V: V.append(pos)
    elif dir == "right":
        if pos[0]+1 >= x:
            inside = False
            continue
        if B[pos[1]][pos[0]+1] == "#":
            dir = "down"
            continue
        else:
            pos = (pos[0]+1, pos[1])
            if pos not in V: V.append(pos)
    elif dir == "down":
        if pos[1]+1 >= y:
            inside = False
            continue
        if B[pos[1]+1][pos[0]] == "#":
            dir = "left"
            continue
        else:
            pos = (pos[0], pos[1]+1)
            if pos not in V: V.append(pos)
    elif dir == "left":
        if pos[0]-1 < 0:
            inside = False
            continue
        if B[pos[1]][pos[0]-1] == "#":
            dir = "up"
            continue
        else:
            pos = (pos[0]-1, pos[1])
            if pos not in V: V.append(pos)

print(V)
print(len(V))
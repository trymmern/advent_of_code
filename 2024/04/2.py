import numpy as np

f = open("input.txt", "r")
B = []
xmasCount = 0
for l in f:
    B.append([c for c in l.strip()])

x = len(B[0])
y = len(B)

def drd(i, j): # down right diagonal
    return y>i+2 and x>j+2 and B[i][j] == "M" and B[i+1][j+1] == "A" and B[i+2][j+2] == "S"
def urd(i, j): # up right diagonal
    return y>i+2 and x>j+2 and B[i+2][j] == "M" and B[i+1][j+1] == "A" and B[i][j+2] == "S"
def dld(i, j): # down left diagonal
    return y>i+2 and x>j+2 and B[i][j+2] == "M" and B[i+1][j+1] == "A" and B[i+2][j] == "S"
def uld(i, j): # up left diagonal
    return y>i+2 and x>j+2 and B[i+2][j+2] == "M" and B[i+1][j+1] == "A" and B[i][j] == "S"

for i in range(y):
    for j in range(x):
        if drd(i, j) and urd(i, j):
            xmasCount += 1
        if drd(i, j) and dld(i, j):
            xmasCount += 1
        if dld(i, j) and uld(i, j):
            xmasCount += 1
        if uld(i, j) and urd(i, j):
            xmasCount += 1


print(xmasCount)


B = np.array(B)
print(B)
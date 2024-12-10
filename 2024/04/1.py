import numpy as np

f = open("input.txt", "r")
board = []
xmasCount = 0
for l in f:
    xmasCount += l.count("XMAS")
    xmasCount += l.count("SAMX")
    board.append([c for c in l.strip()])

xLen = len(board[0])
yLen = len(board)

for i in range(yLen):
    for j in range(xLen):
        if yLen>i+3 and board[i][j] == "X" and board[i+1][j] == "M" and board[i+2][j] == "A" and board[i+3][j] == "S": # vertical down
            xmasCount += 1
        if yLen>i+3 and board[i][j] == "S" and board[i+1][j] == "A" and board[i+2][j] == "M" and board[i+3][j] == "X": # vertical up
            xmasCount += 1
        if yLen>i+3 and xLen>j+3 and board[i][j] == "X" and board[i+1][j+1] == "M" and board[i+2][j+2] == "A" and board[i+3][j+3] == "S": # diagonal down right
            xmasCount += 1
        if yLen>i+3 and xLen>j+3 and board[i][j] == "S" and board[i+1][j+1] == "A" and board[i+2][j+2] == "M" and board[i+3][j+3] == "X": # diagonal up left
            xmasCount += 1
        if yLen>i+3 and j-3>=0 and board[i][j] == "X" and board[i+1][j-1] == "M" and board[i+2][j-2] == "A" and board[i+3][j-3] == "S": # diagonal down left
            xmasCount += 1
        if yLen>i+3 and j-3>=0 and board[i][j] == "S" and board[i+1][j-1] == "A" and board[i+2][j-2] == "M" and board[i+3][j-3] == "X": # diagonal up right
            xmasCount += 1


print(xmasCount)


board = np.array(board)
print(board)
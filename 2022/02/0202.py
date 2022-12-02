f = open("input.txt", "r")

# A = 1 (rock)
# B = 2 (paper)
# C = 3 (scissors)

# W, Z = 6
# D, Y = 3
# L, X = 0

x = { 'B': 1, 'A': 3, 'C': 2 } # loss
y = { 'C': 3, 'B': 2, 'A': 1 } # draw
z = { 'A': 2, 'C': 1, 'B': 3 } # win

def main():
    score = 0;
    for x in f:
        match = x.replace("\n", "").split(" ");
        score += getScore(match)
    print(score);
        

def getScore(match:list[int]) -> int:
    match match[1]:
        case 'X':
            return x[match[0]] + 0;
        case 'Y':
            return y[match[0]] + 3;
        case 'Z':
            return z[match[0]] + 6;
        case _:
            print("No matches wuuuut???");

main();
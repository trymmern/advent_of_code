f = open("input.txt", "r")

# A, X = 1 (rock)
# B, Y = 2 (paper)
# C, Z = 3 (scissors)

# W = 6
# D = 3
# L = 0

x = { 'B': 0, 'A': 3, 'C': 6 }
y = { 'C': 0, 'B': 3, 'A': 6 }
z = { 'A': 0, 'C': 3, 'B': 6 }

def main():
    score = 0;
    for x in f:
        match = x.replace("\n", "").split(" ");
        score += getScore(match)
    print(score);
        

def getScore(match:list[int]) -> int:
    match match[1]:
        case 'X':
            return x[match[0]] + 1;
        case 'Y':
            return y[match[0]] + 2;
        case 'Z':
            return z[match[0]] + 3;
        case _:
            print("No matches wuuuut???");

main();
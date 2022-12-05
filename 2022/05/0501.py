#                         [R] [J] [W]
#             [R] [N]     [T] [T] [C]
# [R]         [P] [G]     [J] [P] [T]
# [Q]     [C] [M] [V]     [F] [F] [H]
# [G] [P] [M] [S] [Z]     [Z] [C] [Q]
# [P] [C] [P] [Q] [J] [J] [P] [H] [Z]
# [C] [T] [H] [T] [H] [P] [G] [L] [V]
# [F] [W] [B] [L] [P] [D] [L] [N] [G]
#  1   2   3   4   5   6   7   8   9 
import re;
f = open("input.txt", "r");

stacks = [['F', 'C', 'P', 'G', 'Q', 'R'], 
          ['W', 'T', 'C', 'P'],
          ['B', 'H', 'P', 'M', 'C'], 
          ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
          ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
          ['D', 'P', 'J'],
          ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
          ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
          ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']];

print(stacks)
for x in f:
    cmd = [int(s) for s in re.findall(r'\b\d+\b', x.strip())];
    for _ in range(cmd[0]):
        stacks[cmd[2]-1].append(stacks[cmd[1]-1].pop());

for i in stacks:
    print(i[len(i)-1])

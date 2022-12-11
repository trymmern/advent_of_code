import sys
from math import prod

f = open("input.txt", "r")
sys.set_int_max_str_digits(10000000)

def main():
    current = 0
    monkeys: list[list[float]] = fill_monkeys()
    inspections: list[int] = [0]*8
    receivers: list(list[int]) = fill_receivers()
    mod = 1
    for r in range(10000):
        f.seek(0,0)
        for l in f:
            l = l.strip()
            cmd = l.split()

            if l == '':
                continue

            if cmd[0] == "Monkey":
                current = int(cmd[1][0])
                print("current: ", current)
            
            if cmd[0] == "Operation:":
                for i in range(len(monkeys[current])):
                    op = l[17:].split()
                    monkeys[current][i] = operation(monkeys[current][i], op)
                    inspections[current] += 1
            
            if cmd[0] == "Test:":
                x = int(cmd[-1])
                for i in range(len(monkeys[current])):
                    if monkeys[current][i] % x == 0:
                        monkeys[receivers[current][0]].append(monkeys[current][i])
                    else:
                        monkeys[receivers[current][1]].append(monkeys[current][i])
                monkeys[current].clear()

        print(f"Round {r} finished: ")

    print(inspections)
    print(prod(sorted(inspections)[-2:]))
                    

def operation(item: int, op: list[str]) -> int:
    if op[1] == '+':
        return item + int(op[2])
    else:
        if op[2] == "old":
            return item * item
        else:
            return item * int(op[2])

def fill_monkeys() -> list[list[float]]:
    return [
        [83, 88, 96, 79, 86, 88, 70],
        [59, 63, 98, 85, 68, 72],
        [90, 79, 97, 52, 90, 94, 71, 70],
        [97, 55, 62],
        [74, 54, 94, 76],
        [58],
        [66, 63],
        [56, 56, 90, 96, 68]
    ]
    

def fill_receivers() -> list[list[int]]:
    c = f.readlines()
    receivers = [
        [get_num(c, 4), get_num(c, 5)],
        [get_num(c, 11), get_num(c, 12)],
        [get_num(c, 18), get_num(c, 19)],
        [get_num(c, 25), get_num(c, 26)],
        [get_num(c, 32), get_num(c, 33)],
        [get_num(c, 39), get_num(c, 40)],
        [get_num(c, 46), get_num(c, 47)],
        [get_num(c, 53), get_num(c, 54)]
    ]

    return receivers

def get_num(l: str, index: int) -> int:
    return int(l[index].strip().split()[-1])

main()
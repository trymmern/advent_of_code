from math import prod

f = open("input.txt", "r")

def main():
    current = 0
    monkeys: list[list[int]] = fill_monkeys()
    inspections: list[int] = [0]*8
    receivers: list(list[int]) = fill_receivers()

    for r in range(20):
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
                    monkeys[current][i] = operation(monkeys[current][i], op)//3
                    inspections[current] += 1
            
            if cmd[0] == "Test:":
                x = int(cmd[-1])
                print(monkeys[current])
                for i in range(len(monkeys[current])):
                    if monkeys[current][i] % x == 0:
                        print(f"{receivers[current][0]} gets {monkeys[current][i]}")
                        monkeys[receivers[current][0]].append(monkeys[current][i])
                    else:
                        print(f"{receivers[current][1]} gets {monkeys[current][i]}")
                        monkeys[receivers[current][1]].append(monkeys[current][i])
                monkeys[current].clear()

        print(f"Monkeys after round {r}: ", monkeys)

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

def fill_monkeys() -> list[list[int]]:
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
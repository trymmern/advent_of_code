import itertools

f = open("input.txt", "r")

def main():
    sums = []
    for l in f:
        R, Q = l.strip().split(":")
        R = int(R)
        Q = [int(n) for n in Q.strip().split(" ")]
        print(R, Q)

        for perm in itertools.permutations(Q):
            for ops in itertools.product(['+', '*'], repeat=len(Q)-1):
                if evaluate_expression(perm, ops) == R:
                    if (R not in sums):
                        print(perm, ops)
                        sums.append(R)
                    break

    print(sum(sums))

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
    return result

main()
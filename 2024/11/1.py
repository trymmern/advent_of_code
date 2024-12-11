f = open("input.txt", "r")

S = [int(s) for l in f for s in l.strip().split()]
print(S)

# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

for i in range(25):
    print(f"Step {i}: {S}")
    new_S = []
    for s in S:
        if s == 0:
            new_S.append(1)
        elif len(str(s)) % 2 == 0:
            s = str(s)
            new_S.append(int(s[:len(s)//2]))
            new_S.append(int(s[len(s)//2:]))
        else:
            new_S.append(s * 2024)
    S = new_S

print(len(S))
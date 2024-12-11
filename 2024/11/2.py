from functools import cache

f = open("input.txt", "r")

S = [int(s) for l in f for s in l.strip().split()]
print(S)

# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

def blink(num):
    if num == 0:
        return [1]
    s = f'{num}'
    l = len(s)
    if l % 2 == 0:
        return [int(n) for n in [s[:l//2], s[l//2:]]]
    else:
        return [num * 2024]

@cache
def count_splits(number, blinks):
    if blinks == 0:
        return 1
    return sum(count_splits(n, blinks - 1) for n in blink(number))

sum = sum(count_splits(s, 75) for s in S)
print(sum)
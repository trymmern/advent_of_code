import re

f = open("input.txt", "r")
numbers = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]

def main():
    sum = 0
    for x in f:
        a, b = '', ''
        foundNums = []
        for n in numbers:
            for found in [(m, str(n[1])) for m in re.finditer(n[0], x)]:
                foundNums.append(found)

        foundNums = sorted(foundNums, key=lambda x: x[0].start())
        nums = [n for n in enumerate(x) if n[1].isdigit()]

        if len(foundNums) == 0:
            a = nums[0][1]
            b = nums[-1][1]
        else:  
            if nums[0][0] < foundNums[0][0].start():
                a = nums[0][1]
            else:
                a = foundNums[0][1]
            if nums[-1][0] > foundNums[-1][0].end()-1:
                b = nums[-1][1]
            else:
                b = foundNums[-1][1]

        print('X:', x)
        print('A:', a, 'B:', b)
        print('Nums:', nums)
        print('Found:', foundNums)

        sum += int(a + b)
    print(sum)

main()
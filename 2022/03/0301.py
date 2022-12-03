import string
f = open("input.txt", "r")

def main ():
    values = getValues()
    print(values)
    score = 0;
    for x in f:
        str1 = x[0:len(x)//2];
        str2 = x[len(x)//2:len(x)];

        common = list(set(str1)&set(str2))
        for l in common:
            score += values[l];
    print(score);


def getValues():
    lc = dict()
    for index, letter in enumerate(string.ascii_lowercase, 1):
        lc[letter] = index

    uc = dict()
    for index, letter in enumerate(string.ascii_uppercase, 27):
        uc[letter] = index

    return lc | uc

main()
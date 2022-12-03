import string
f = open("input.txt", "r")

def main ():
    values = getValues()
    score = 0;
    group: list[str] = [];
    for x in f:
        group.append(x.replace("\n", ""));
        if (len(group) < 3):
            continue;
        common = list(set(group[0])&set(group[1])&set(group[2]));
        for l in common:
            score += values[l];
        group.clear();
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
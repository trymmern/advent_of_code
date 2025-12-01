from functools import cmp_to_key

f = open("input_ex.txt", "r")

rules = []
isValid = True
I = []
for l in f:
    if "|" in l:
        line = l.strip().split("|")
        rules.append((int(line[0]), int(line[1])))
        continue
    
    if l.strip() == "": continue
    isValid = True
    
    line = l.strip().split(",")
    U = [int(x) for x in line]
    
    for i in range(len(U)):
        for r1, r2 in rules:
            if U[i] not in [r1, r2] or U[i-1] not in [r1, r2]:
                continue
            if (r2 == U[i] and r1 in U[i:]) or (r1 == U[i] and r2 in U[:i]):
                isValid = False
                I.append(U)
                break
        if not isValid: break

print(rules)
print(I)

def compare(item1, item2):
    for r1, r2 in rules:
        if item1 == r1 and item2 == r2:
            return 0
        if item1 == r2 and item2 == r1:
            return 1

#I2 = []
for i in I:
    #I2.append(i.sort(key=compare))
    sorted(i, key=cmp_to_key(lambda i1, i2: compare(i1, i2)))
print(I)
f = open("input_ex.txt", "r")

rules = []
isValid = True
M = []
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
            if r2 == U[i] and r1 in U[i:]:
                isValid = False
                break
        if not isValid: break
    
    if isValid:
        M.append(U[int((len(U)/2)-.5)])

# print(rules)
print(M)
print(sum(M))
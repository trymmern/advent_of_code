import re

f = open("input.txt", "r")
data = f.read()

pattern = r"mul\(\d+,\d+\)|do\(+\)|don\'t\(+\)"
matches = re.findall(pattern, data)

sum = 0
do = True
for m in matches:
    if m == "do()":
        do = True
        continue
    if m == "don't()":
        do = False
        continue
    
    if do:
        m = m.replace("mul(", "").replace(")", "")
        a, b = m.split(",")
        sum += int(a) * int(b)
print(sum)
import re

f = open("input.txt", "r")
data = f.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, data)

sum = 0
for m in matches:
    m = m.replace("mul(", "").replace(")", "")
    a, b = m.split(",")
    sum += int(a) * int(b)
print(sum)
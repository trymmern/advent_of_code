import re

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

g = []
for i, row in enumerate(data_input):
    matches = re.finditer(r"\d+", row)
    length = len(row)
    for match in matches:
        number = match.group()
        idx = [match.start(), match.end()]
        for j in range(int(idx[0])-1, int(idx[1])+1):
            # Check number in actual row
            if i > 0 and j < length:
                if data_input[i][j] == "*" and not data_input[i][j].isnumeric():
                    g.append([int(number), (i, j)])
                    break
            # Check number in upper row
            if i > 0 and j < length:
                if data_input[i-1][j] == "*" and not data_input[i-1][j].isnumeric():
                    g.append([int(number), (i-1, j)])
                    break
            # Check number in lower row
            if i < length - 1 and j < length:
                if data_input[i+1][j] == "*" and not data_input[i+1][j].isnumeric():
                    g.append([int(number), (i+1, j)])
                    break

# filter non-unique coordinates
tuple_frequency = {}
for item in g:
    _, tpl = item
    tuple_frequency[tpl] = tuple_frequency.get(tpl, 0) + 1
filtered_data = [item for item in g if tuple_frequency[item[1]] > 1]

# multiply values with same coordinates
couples = {}
for gear in filtered_data:
    if couples.get(gear[1]) is not None:
        couples[gear[1]] *= gear[0]
    else:
        couples[gear[1]] = gear[0]
print(sum(list(couples.values())))
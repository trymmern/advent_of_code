f = open("01-input.txt", "r")

max: list[int] = [0,0,0];
counter = 0;
for x in f:
    if x.strip() == "":
        if any(i < counter for i in max):
            max[max.index(min(max))] = counter;
        counter = 0;
        continue;
    
    counter += int(x);
print(sum(max));

f.close();
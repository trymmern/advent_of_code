f = open("01-input.txt", "r")

max = 0;
counter = 0;
for x in f:
    if x.strip() == "":
        if counter > max:
            max = counter;
        counter = 0;
        continue;
    
    counter += int(x);
print(max);

f.close();
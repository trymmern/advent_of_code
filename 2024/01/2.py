f = open("input.txt", "r")

a = []
b = [];

for l in f:
    nums = l.split("   ");
    a.append(int(nums[0]));
    b.append(int(nums[1]));

sum = 0
for i in range(len(a)):
    count = 0
    for j in range(len(b)):
        if (a[i] == b[j]):
            count += 1
    sum += a[i] * count

print(sum)
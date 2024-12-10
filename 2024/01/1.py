f = open("input.txt", "r")

a = []
b = [];

for l in f:
    nums = l.split("   ");
    a.append(int(nums[0]));
    b.append(int(nums[1]));

a.sort()
b.sort()

sum: int = sum([abs(a[i] - b[i]) for i in range(len(a))])
print(sum)
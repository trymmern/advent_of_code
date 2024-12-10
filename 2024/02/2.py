f = open("input.txt", "r")

safeSum = 0
for l in f:
    nums = [int(n) for n in l.split(" ")]

    safeAsc = [nums[i] > nums[i - 1] and 0 < nums[i] - nums[i-1] < 4 for i in range(1, len(nums))]
    safeDsc = [nums[i] < nums[i - 1] and 0 < nums[i-1] - nums[i] < 4 for i in range(1, len(nums))]

    if safeAsc.count(True) == len(safeAsc) - 1 or safeDsc.count(True) == len(safeDsc) - 1:
        print("Asc: ", safeAsc)
        print("Desc:", safeDsc)

    if safeAsc.count(True) >= len(safeAsc) - 1 or safeDsc.count(True) >= len(safeDsc) - 1:
        safeSum += 1
    

print(safeSum)
f = open("input.txt", "r")

safeSum = 0
for l in f:
    nums = [int(n) for n in l.split(" ")]
    safeAsc = all([nums[i] > nums[i - 1] and 0 < nums[i] - nums[i-1] < 4 for i in range(1, len(nums))])
    safeDsc = all([nums[i] < nums[i - 1] and 0 < nums[i-1] - nums[i] < 4 for i in range(1, len(nums))])
    
    if safeDsc or safeAsc:
        safeSum += 1

print(safeSum)
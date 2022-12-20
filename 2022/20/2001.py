from collections import deque

f = open("input.txt", "r")

def move_element(key, val):
    index = new_nums.index((key, val))
    
    new_nums.remove((key, val))
    new_nums.rotate(-val)
    new_nums.insert(index, (key, val))
    

nums = [(i, int(l.strip())) for i, l in enumerate(f)]
new_nums = deque(nums.copy())
zero = tuple()

for key, val in nums:
    if val == 0:
        zero = (key, val)
    move_element(key, val)

    if key == 0:
        print(new_nums[0])
        print(new_nums[2144])

i1 = new_nums[(new_nums.index(zero)+1000) % len(new_nums)][1]
i2 = new_nums[(new_nums.index(zero)+2000) % len(new_nums)][1]
i3 = new_nums[(new_nums.index(zero)+3000) % len(new_nums)][1]

print(i1, i2, i3)
print(sum([i1, i2, i3]))
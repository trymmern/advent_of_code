f = open("input.txt", "r")

def main():
    sum = 0
    for x in f:
        nums = [n[1] for n in enumerate(x) if n[1].isdigit()]
        sum += int(nums[0] + nums[-1])
    print(sum)
main()
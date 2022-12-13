from ast import literal_eval

f = open("input.txt", "r")

def main():
    indeces = []
    left, right = [], []
    index = 0
    for i, l in enumerate(f, 1):
        l = l.strip()

        if l == '':
            continue
        
        if i % 3 == 1:
            left = literal_eval(l)
            continue
        if i % 3 == 2:
            right = literal_eval(l)
            index += 1
            
        if check_packets(left, right) > 0:
            indeces.append(index)
        
    print(indeces)
    print("Answer: ", sum(indeces))

def check_packets(left, right) -> int:
    for i in range(0, len(left)):
        if i >= len(right):
            return -1
        
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
            else:
                continue
        elif isinstance(left[i], list) and isinstance(right[i], list):
            res = check_packets(left[i], right[i])
            if res != 0:
                return res
        elif isinstance(left[i], list):
            res = check_packets(left[i], [right[i]])
            if res != 0:
                return res
        elif isinstance(right[i], list):
            res = check_packets([left[i]], right[i])
            if res != 0:
                return res

    if len(left) == len(right):
        return 0
    return 1

main()
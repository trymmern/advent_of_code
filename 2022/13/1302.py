from ast import literal_eval

f = open("input.txt", "r")

def main():
    left, right = [], []
    decoder_key1 = [[2]]
    decoder_key2 = [[6]]
    packets = [decoder_key1, decoder_key2]
    for i, l in enumerate(f, 1):
        l = l.strip()

        if l == '':
            continue
        
        if i % 3 == 1:
            left = literal_eval(l)
            packets.append(left)
            continue
        if i % 3 == 2:
            right = literal_eval(l)
            packets.append(right)
    
    packets = bubble_sort(packets)

    index1 = packets.index(decoder_key1) + 1
    index2 = packets.index(decoder_key2) + 1

    print(index1, index2)
    print("Answer: ", index1 * index2)

def bubble_sort(packets: list) -> list:
    j = 0
    for i in range(len(packets)-1):
        for j in range(0, len(packets)-i-1):
            if check_packets(packets[j], packets[j + 1]) <= 0:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    return packets


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
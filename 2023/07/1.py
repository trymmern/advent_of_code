from collections import Counter

D = open("input.txt", "r").read().strip().split('\n')

hands = [(h, int(b)) for h, b in [x.split() for x in D]]
print(len(hands))

# score for each card
cards = {str(i): i for i in range(2, 10)}
cards.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

# merge sort -------------------------------------------------------------------
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)

    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + i] for i in range(n2)]

    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if is_lower(L[i], R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

def is_lower(h1, h2):

    counter1 = Counter(h1[0])
    counter2 = Counter(h2[0])

    max_num1 = max(counter1.values())
    max_num2 = max(counter2.values())

    if max_num1 < max_num2:
        return True
    elif max_num1 > max_num2:
        return False
    else: # max_num1 == max_num2
        # Case where full house is compared with three of a kind
        if max_num1 == 3 and max_num2 == 3:
            if min(counter1.values()) < min(counter2.values()):
                return True
            elif min(counter1.values()) > min(counter2.values()):
                return False
        
        # Cases where the highest amount of same cards are the same
        for i in range(len(h1[0])):
            if cards[h1[0][i]] < cards[h2[0][i]]:
                return True
            elif cards[h1[0][i]] > cards[h2[0][i]]:
                return False
            else:
                continue

merge_sort(hands, 0, len(hands)-1)

S = []
for i in range(len(hands)):
    S.append(int(hands[i][1])*(i+1))
print(sum(S))
# merge sort -------------------------------------------------------------------


# short solution ---------------------------------------------------------------
def get_strength(hand):
    strenght = tuple(sorted(Counter(hand).values(), reverse=True))
    print(strenght)
    return strenght

H = hands.sort(key=lambda h: get_strength(h[0]))
print(sum(hand[1] * (i+1) for i, hand in enumerate(hands)))
# short solution ---------------------------------------------------------------

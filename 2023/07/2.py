from collections import Counter

D = open("input.txt", "r").read().strip().split('\n')

# score for each card
cards = {str(i): i for i in range(2, 10)}
cards.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

def get_numerical(hand):
    return tuple(cards[c] for c in hand)

hands = [(get_numerical(h), int(b)) for h, b in [x.split() for x in D]]


def get_strength(hand):
    jokers = hand.count(11)
    hand_without_jokers = tuple([c for c in hand if c != 11])
    strength = list(sorted(Counter(hand_without_jokers).values(), reverse=True))

    if not strength:
        strength = (5,)
    else:
        strength[0] += jokers

    strength = tuple(strength)
    new_hand = tuple(1 if c == 11 else c for c in hand)
    return strength, new_hand

hands.sort(key=lambda h: get_strength(h[0]))
print(sum(hand[1] * (i+1) for i, hand in enumerate(hands)))
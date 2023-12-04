from collections import deque

f = open("input.txt", "r")

def main():
    deq = deque()
    cards: dict = {}
    for x in f:
        card_num = [int(n) for n in x.strip().split(':')[0].strip().split(' ') if n.isnumeric()][0]
        game = x.strip().split(':')[1].split('|')
        win_con = [int(w) for w in game[0].strip().split(' ') if w.isnumeric()]
        numbers = [int(num) for num in game[1].strip().split(' ') if num.isnumeric()]

        cards[card_num] = (win_con, numbers)
        deq.append(card_num)
        
    total = 0
    while len(deq) > 0:
        total += 1
        card_num = deq.popleft()
        win_con, numbers = cards[card_num]
        game_sum = 0
        for n in numbers:
            if n in win_con:
                game_sum += 1
                if card_num+game_sum in cards.keys():
                    deq.append(card_num+game_sum)
        
        print(f'Card: {card_num} | Sum: {total}')

    print(total)



main()
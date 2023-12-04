f = open("input.txt", "r")

def main():
    sum = 0
    for x in f:
        game = x.strip().split(':')[1].split('|')
        win_con = [w for w in game[0].strip().split(' ') if w.isnumeric()]
        numbers = [num for num in game[1].strip().split(' ') if num.isnumeric()]

        game_sum = 0
        for n in numbers:
            if n in win_con:
                if game_sum == 0:
                    print(n)
                    game_sum += 1
                else:
                    game_sum *= 2
        sum += game_sum
    print(sum)

main()
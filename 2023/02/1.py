f = open("input.txt", "r")


max_r, max_g, max_b = 12, 13, 14

def main():
    sum = 0
    for x in f:
        game = x.strip().split(':')[0].split(' ')[1]
        x = x.strip().split(':')[1]
        grabs = [i.strip().split(',') for i in x.strip().split(';')]

        possible = True
        for grab in grabs:
            for g in grab:
                print(game, sum)
                if not is_possible(g):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum += int(game)
    return sum


def is_possible(g) -> bool:
    if 'red' in g:
        if max_r < int(g.strip().split(' ')[0]):
            print('red', g.strip().split(' ')[0], max_r)
            return False
    elif 'green' in g:
        if max_g < int(g.strip().split(' ')[0]):
            print('green', g.strip().split(' ')[0], max_g)
            return False
    elif 'blue' in g:
        if max_b < int(g.strip().split(' ')[0]):
            print('blue', g.strip().split(' ')[0], max_b)
            return False
    return True

print(main())
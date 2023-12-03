f = open("input.txt", "r")

def main():
    sum = 0
    for x in f:
        game = x.strip().split(':')[0].split(' ')[1]
        x = x.strip().split(':')[1]
        grabs = [i.strip().split(',') for i in x.strip().split(';')]

        min_r, min_g, min_b = 0, 0, 0
        for grab in grabs:
            for g in grab:
                if 'red' in g:
                    min_r = max(min_r, int(g.strip().split(' ')[0]))
                elif 'green' in g:
                    min_g = max(min_g, int(g.strip().split(' ')[0]))
                elif 'blue' in g:
                    min_b = max(min_b, int(g.strip().split(' ')[0]))
        sum += min_r * min_g * min_b
        
    return sum

print(main())
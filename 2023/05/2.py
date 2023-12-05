f = open("input.txt", "r").read().strip()

def main():
    parts = f.split('\n\n')
    seeds, *maps = parts

    print(f'Seeds: {seeds}')
    print(f'Maps: {maps}')


    S = []
    si = 0
    while si < len(seeds):
        st, sz = int(seeds[si]), int(seeds[si+1])
        si += 2
        R = [(st, st+sz)]
        
        next_val = s
        for m in maps:
            M = m.split('\n')
            next_val = find_dest(next_val, M[1:])
        S.append(next_val)
    
    print(f'min of {S} is {min(S)}')
            

def find_dest(s: int, m) -> int:
    for line in m:
        d, src, r = [int(x) for x in line.split()]
        if src <= s <  src+r:
            return d + (s - src)
    return s

main()

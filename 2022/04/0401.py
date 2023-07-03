f = open("input.txt", "r");

def main():
    score = 0;
    for x in f:
        x1, x2 = x.strip().split(",");

        x1_start, x1_end = map(int, x1.split("-"))
        x2_start, x2_end = map(int, x2.split("-"))

        if x2_start <= x1_start and x1_end <= x2_end or (x1_start <= x2_start and x2_end <= x1_end):
            score += 1;

    print(score);

main();
f = open("input.txt", "r");

def main():
    score = 0;
    for x in f:
        x1, x2 = x.strip().split(",");

        x1_start, x1_end = map(int, x1.split("-"))
        x2_start, x2_end = map(int, x2.split("-"))
        print(x1, x2)

        if max(x1_start, x2_start) <= min(x1_end, x2_end):
            score += 1;
            print("SCORE UPDATED. NEW SCORE: ", score)

    print(score);

main();
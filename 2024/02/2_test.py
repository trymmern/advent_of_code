def check_safe(report):
    safe = 0
    incr = False
    decr = False
    for i in range(len(report) - 1):
        safe = 1
        diff = report[i + 1] - report[i]
        if diff > 0:
            incr = True
        if diff < 0:
            decr = True
        if (incr == True and decr == True) or not (0 < abs(diff) < 4):
            safe = 0
            break
    return safe

with open('input.txt', 'r') as file_in:

    safe_count = 0
    for rep in file_in:
        report = [int(level) for level in rep.split()]
        incr = False
        decr = False
        safe = check_safe(report)
        if safe == 0:
            for i in range(len(report)):
                temp = report.pop(i)
                safe = check_safe(report)
                if safe == 1:
                    break
                report.insert(i, temp)
        safe_count += safe
print(safe_count)
# Verify ascending
def check_asc(report_in, dampen=0):
    report = list(report_in)

    while True:
        tmp = min(report)
        safe = True

        for i in range(0, len(report)):
            if report[i] < tmp:
                safe = False
                break
            tmp = report[i]

        if dampen and not safe:
            dampen -= 1
            report.pop(i-1)
            continue
        else:
            return safe
        

# Verify descending
def check_desc(report_in, dampen=0):
    report = list(report_in)

    while True:
        tmp = max(report)
        safe = True

        for i in range(0, len(report)):
            if report[i] > tmp:
                safe = False
                break
            tmp = report[i]

        if dampen and not safe:
            dampen -= 1
            report.pop(i-1)
            continue
        else:
            return safe


# Verify diffs between adjacent numbers are 1 <= n <= 3
def check_diffs(report_in, dampen=0):
    report = list(report_in)
    while True:
        safe = True
        for i in range(1, len(report)-1):
            low_diff = abs(report[i] - report[i-1])
            high_diff = abs(report[i] - report[i+1])
            if ((low_diff < 1) or (low_diff > 3)) or ((high_diff < 1) or (high_diff > 3)):
                safe = False
                break
        
        if dampen and not safe:
            dampen -= 1
            report.pop(i)
            continue
        else:
            return safe

# Load levels from file
levels = list()
with open(".\\input.txt", "r") as filein:
    levels = filein.readlines()
levels = [i.replace("\n", "").split(" ") for i in levels]
for i in range(0, len(levels)):
    levels[i] = [int(j) for j in levels[i]]

dampen = 1

print(f"Number of reports: {len(levels)}")
levels = [i for i in levels if (check_asc(i, dampen=dampen) or check_desc(i, dampen=dampen))]
print(f"Number of ascending/descending reports: {len(levels)}")
levels = [i for i in levels if check_diffs(i, dampen=dampen)]
print(f"Number of safe reports: {len(levels)}")
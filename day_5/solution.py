# Check a given rule against an array
def check_rule(rulestr, arr):
    arr = list(arr)
    pre_num, post_num = [int(i) for i in rulestr.split("|")]
    if (pre_num in arr) and (post_num in arr) and (arr.index(post_num) < arr.index(pre_num)):
        return False
    return True

# Check a rule list against an array
def check_rules(rules, arr):
    for i in rules:
        if check_rule(i, arr) == False:
            return False
    return True

# Recursive correction
def do_correction(rules, arr, idx, result):
    if idx >= len(arr): return result
    tmp_num = arr[idx]

    for i in range(0, len(result)+1):
        tmp_arr = list(result)
        tmp_arr.insert(i, tmp_num)
        if not check_rules(rules, tmp_arr):
            continue
        tmp_result = do_correction(rules, arr, idx+1, tmp_arr)
        if tmp_result != None:
            return tmp_result
    return None
        


# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()

# Input preparation
raw_rules, raw_updates = raw_data.split("\n\n")
rules = raw_rules.split("\n")
str_updates = raw_updates.split("\n")
updates = [i.split(",") for i in str_updates]

for i in range(0, len(updates)):
    for j in range(0, len(updates[i])):
        updates[i][j] = int(updates[i][j])

# Solution
correct_updates = list()
corrected_updates = list()

for i in updates:
    if check_rules(rules, i):
        correct_updates.append(i)
        pass
    else:
        corrected = do_correction(rules, i, 0, list())
        if (check_rules(rules, corrected)):
            corrected_updates.append(corrected)

print(f"Initial input: {len(updates)}")
print(f"Cleaned input: {len(correct_updates)}")

middle_total = 0

for i in correct_updates:
    middle_total += i[len(i) // 2]

print(f"Middle total: {middle_total}")

middle_total = 0

for i in corrected_updates:
    middle_total += i[len(i) // 2]

print(f"Middle total (corrected): {middle_total}")
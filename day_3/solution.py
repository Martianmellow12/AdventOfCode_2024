import re

with open("input.txt", "r") as filein:
    data = filein.read()

regex = "mul\(\d\d?\d?,\d\d?\d?\)"

# Part 1
total = 0
results = re.findall(regex, data)
for i in list(results):
    i = i.replace("mul(", "")
    i = i.replace(")", "")
    i = i.split(",")
    total += int(i[0]) * int(i[1])

print(f"Sum total: {total}")


# Part 2
modded_data = data + "DEADBEEF"
stripped_data = str()
active = True
for i in range(0, len(data)):
    if modded_data[i:i+4] == "do()": active = True
    if modded_data[i:i+7] == "don't()": active = False
    if active: stripped_data += modded_data[i]

total = 0
results = re.findall(regex, stripped_data)
for i in list(results):
    i = i.replace("mul(", "")
    i = i.replace(")", "")
    i = i.split(",")
    total += int(i[0]) * int(i[1])

print(f"Sum total (modded): {total}")
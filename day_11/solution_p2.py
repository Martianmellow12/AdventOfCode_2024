# Iterate stones
def iter_stones(stones):
    new_stones = dict()

    for i in stones.keys():
        if i == "0":
            if "1" not in new_stones.keys(): new_stones["1"] = stones[i]
            else: new_stones["1"] += stones[i]
        elif (len(i) % 2) == 0:
            key1 = str(int(i[:len(i)//2]))
            key2 = str(int(i[len(i)//2:]))
            if key1 not in new_stones.keys(): new_stones[key1] = stones[i]
            else: new_stones[key1] += stones[i]
            if key2 not in new_stones.keys(): new_stones[key2] = stones[i]
            else: new_stones[key2] += stones[i]
        else:
            key = str(int(i)*2024)
            if key not in new_stones.keys(): new_stones[key] = stones[i]
            else: new_stones[key] += stones[i]

    return new_stones


# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()

stones = dict()
for i in raw_data.split(" "):
    if i not in stones.keys(): stones[i] = 1
    else: stones[i] += 1

for i in range(0, 75):
    stones = iter_stones(stones)

num_stones = 0
for i in stones.keys(): num_stones += stones[i]

print(f"Number of stones: {num_stones}")
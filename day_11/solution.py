# Iterate stones
def iter_stones(stones):
    new_stones = list()
    for i in stones:
        if i == "0": new_stones.append("1")
        elif (len(i) % 2) == 0:
            new_stones.append(str(int(i[:len(i)//2])))
            new_stones.append(str(int(i[len(i)//2:])))
        else:
            new_stones.append(str(int(i) * 2024))
    return new_stones

# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()

stones = raw_data.split(" ")

for i in range(0, 25):
    stones = iter_stones(stones)

print(f"Number of stones: {len(stones)}")
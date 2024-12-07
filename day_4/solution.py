# Get the array size
def get_arr_size(arr):
    width = len(arr[0])
    height = len(arr)
    return [width, height]

# Get the character at a position
def get_pos(arr, x, y):
    return arr[y][x]

# Convert a linear index to a coordinate
def idx_to_pos(arr, idx):
    width, height = get_arr_size(arr)
    x = idx % width
    y = idx // width
    return [x, y]

# Check a direction for a match
def check_direction(arr, x, y, width, height, dir):
    x_inc = dir[0]
    y_inc = dir[1]
    max_x_offset = x + (3*x_inc)
    max_y_offset = y + (3*y_inc)

    # Boundary checks
    if (max_x_offset >= width) or (max_x_offset < 0): return False
    if (max_y_offset >= height) or (max_y_offset < 0): return False

    # Search
    chars = str()
    for i in range(1, 4):
        chars += get_pos(arr, x+(i*x_inc), y+(i*y_inc))

    if chars == "MAS": return True
    return False

# Check a given X for any matches
def check_matches(arr, x, y):
    match_count = 0
    directions = list()

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not ((i == 0) and (j == 0)): directions.append([i, j])

    width, height = get_arr_size(arr)

    for i in directions:
        if check_direction(arr, x, y, width, height, i):
            match_count += 1

    return match_count


# Load the input
with open("input.txt", "r") as filein:
    data = filein.read()

# Convert the input into a 2D array
data_arr = data.split("\n")
for i in range(0, len(data_arr)):
    data_arr[i] = list(data_arr[i])

# Iterate through the array
matches = 0

for x in range(0, get_arr_size(data_arr)[0]):
    for y in range(0, get_arr_size(data_arr)[1]):
        if data_arr[y][x] == "X": matches += check_matches(data_arr, x, y)

print(f"Number of matches: {matches}")
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

# Convert a 3x3 position into a string
# Ex.   ABC
#       DEF  ->  ABCDEFGHI
#       GHI
def pos_to_str(arr, x, y):
    width, height = get_arr_size(arr)
    if (x + 2) >= width: return None
    if (y + 2) >= height: return None

    result = get_pos(arr, x, y) + \
             get_pos(arr, x+2, y) + \
             get_pos(arr, x+1, y+1) + \
             get_pos(arr, x, y+2) + \
             get_pos(arr, x+2, y+2)

    return result

# Check a position for matches
def check_matches(arr, x, y):
    match_strs = [
        "MMASS",
        "MSAMS",
        "SMASM",
        "SSAMM"
    ]
    arr_str = pos_to_str(arr, x, y)
    return arr_str in match_strs

# Load the input
with open("input.txt", "r") as filein:
    data = filein.read()

# Convert the input into a 2D array
data_arr = data.split("\n")
for i in range(0, len(data_arr)):
    data_arr[i] = list(data_arr[i])

# Iterate through the array
matches = 0

for y in range(0, get_arr_size(data_arr)[1]):
    for x in range(0, get_arr_size(data_arr)[0]):
        if check_matches(data_arr, x, y): matches += 1

print(f"Number of matches: {matches}")
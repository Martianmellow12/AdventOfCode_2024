# Get map size
def get_map_size(map_arr):
    return [len(map_arr[0]), len(map_arr)]

# Locate trailheads
def loc_trailheads(map_arr):
    trailheads = list()
    for y in range(0, len(map_arr)):
        for x in range(0, len(map_arr[y])):
            if map_arr[y][x] == 0: trailheads.append([x, y])
    return trailheads

# Find trails
def find_trails(map_arr, pos, map_size, trail_ends=list(), problem_part=1):
    num_trails = 0
    x_pos = pos[0]
    y_pos = pos[1]
    map_w = map_size[0]
    map_h = map_size[1]

    # Exit condition
    if map_arr[pos[1]][pos[0]] == 9:
        if (problem_part == 1) and (not pos in trail_ends): trail_ends.append(pos)
        if (problem_part == 2): trail_ends.append(pos)
        return

    # Check for an increase in each direction
    if ((y_pos - 1) >= 0) and (map_arr[y_pos-1][x_pos] == (map_arr[y_pos][x_pos] + 1)): find_trails(map_arr, [x_pos, y_pos-1], map_size, trail_ends, problem_part)
    if ((y_pos + 1) < map_h) and (map_arr[y_pos+1][x_pos] == (map_arr[y_pos][x_pos] + 1)): find_trails(map_arr, [x_pos, y_pos+1], map_size, trail_ends, problem_part)
    if ((x_pos - 1) >= 0) and (map_arr[y_pos][x_pos-1] == (map_arr[y_pos][x_pos] + 1)): find_trails(map_arr, [x_pos-1, y_pos], map_size, trail_ends, problem_part)
    if ((x_pos + 1) < map_w) and (map_arr[y_pos][x_pos+1] == (map_arr[y_pos][x_pos] + 1)): find_trails(map_arr, [x_pos+1, y_pos], map_size, trail_ends, problem_part)
    return trail_ends


# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()
map_arr = raw_data.split("\n")
for i in range(0, len(map_arr)):
    map_arr[i] = [int(j) for j in map_arr[i]]

# Calculate trail scores
p1_score = 0
p2_score = 0
for i in loc_trailheads(map_arr):
    trail_ends = list()
    find_trails(map_arr, i, get_map_size(map_arr), trail_ends, problem_part=1)
    p1_score += len(trail_ends)

    trail_ends = list()
    find_trails(map_arr, i, get_map_size(map_arr), trail_ends, problem_part=2)
    p2_score += len(trail_ends)

print(f"Part 1 score: {p1_score}")
print(f"Part 2 score: {p2_score}")

import copy
import cProfile

# Duplicate array
def dup_arr(arr):
    #result = list()
    #for i in arr:
    #    result.append(list(i))
    return [i[:] for i in arr]

# Get array size
def get_arr_size(arr):
    width = len(arr[0])
    height = len(arr)
    return [width, height]

# Locate guard
def locate_guard(arr):
    guard_vals = ["<", ">", "^", "v"]
    for y in range(0, len(arr)):
        for g in guard_vals:
            if g in arr[y]:
                return [arr[y].index(g), y]
        #for x in range(0, len(arr[y])):
        #    if arr[y][x] in guard_vals: return [x, y]

# Step guard
def step_guard(arr, g_pos, allow_blocks=True):
    rotation_dict = {
        "<" : "^",
        "^" : ">",
        ">" : "v",
        "v" : "<"
    }

    w, h = get_arr_size(arr)
    gx, gy = g_pos
    g = arr[gy][gx]

    # Select a translation
    new_gx = gx
    new_gy = gy
    if g == "<": new_gx = gx - 1
    if g == ">": new_gx = gx + 1
    if g == "^": new_gy = gy - 1
    if g == "v": new_gy = gy + 1

    # Boundary checks
    if (new_gx < 0) or (new_gx >= w) or (new_gy < 0) or (new_gy >= h):
        arr[gy][gx] = "X"
        return None
    
    # Check if a block at the new location would create a loop
    loop_loc = False
    if arr[new_gy][new_gx] != "#" and allow_blocks:
        tmp_arr = dup_arr(arr)
        tmp_arr[new_gy][new_gx] = "#"
        tmp_g_pos = list(g_pos)
        visited_locs = list()

        while True:
            new_loc = step_guard(tmp_arr, tmp_g_pos, allow_blocks=False)
            if new_loc == None:
                break
            if (new_loc in visited_locs):
                loop_loc = True
                break
            visited_locs.append(new_loc)
            tmp_g_pos = new_loc[0:2]

    # Rotation check
    if arr[new_gy][new_gx] == "#":
        arr[gy][gx] = rotation_dict[g]
        return [gx, gy, rotation_dict[g], loop_loc]

    # Lift guard
    arr[gy][gx] = "X"

    # Place guard
    arr[new_gy][new_gx] = g
    return [new_gx, new_gy, g, loop_loc]

# Load input
with open("input.txt", "r") as filein:
    raw_data = filein.read()
input_arr = raw_data.split("\n")
for i in range(0, len(input_arr)):
    input_arr[i] = [i for i in input_arr[i]]
init_input_arr = dup_arr(input_arr)

# Step to completion
distinct_locs = list()
counter = 0
init_g_pos = locate_guard(input_arr)
g_pos = init_g_pos
while True:
    #if counter == 15: break
    counter += 1
    print(f"Stepping: {counter}")
    step_result = step_guard(input_arr, g_pos, allow_blocks=False)
    if step_result == None:
        distinct_locs.append(g_pos)
        break
    if step_result[0:2] != init_g_pos:
        distinct_locs.append(step_result[0:2])
    g_pos = step_result[0:2]

# Check for infinite loops
loop_locs = 0
loop_loc_arr = list()
counter = 0
for i in distinct_locs:
    counter += 1
    print(f"Checking {counter} ({loop_locs} loops found, {len(loop_loc_arr)} unique)")
    visited_locs = list()
    g_pos = init_g_pos
    tmp_arr = dup_arr(init_input_arr)
    tmp_arr[i[1]][i[0]] = "#"

    while True:
        new_loc = step_guard(tmp_arr, g_pos, allow_blocks=False)
        if new_loc == None:
            break
        if new_loc[0:3] in visited_locs:
            print("FOUND LOOP")
            loop_locs += 1
            if i not in loop_loc_arr:
                loop_loc_arr.append(i)
            break
        visited_locs.append(new_loc[0:3])
        g_pos = new_loc[0:2]

# Count distinct locations visited
loc_count = 0
for i in input_arr:
    loc_count += i.count("X")
print(f"Disctinct locations: {loc_count}")
print(f"Loop locations: {loop_locs} ({len(loop_loc_arr)} unique)")

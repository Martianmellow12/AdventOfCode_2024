# Print out the map
def print_map(map):
    for y in map:
        for x in y:
            print(x, end="")
        print("")

# Upscale a map to use double width
def upscale_map(map):
    new_map = list()
    for i in map:
        new_map.append(list())
        for j in i:
            if j == "#": new_map[-1] += ["#", "#"]
            if j == "O": new_map[-1] += ["[", "]"]
            if j == ".": new_map[-1] += [".", "."]
            if j == "@": new_map[-1] += ["@", "."]
    return new_map

# Calculate the sum of all box coordinates
def calc_box_coord_sum(map, box_char="O"):
    coord_sum = 0
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == box_char: coord_sum += (100*y) + x
    return coord_sum

# Locate the robot on the map
def locate_robot(map):
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "@": return [x, y]
    return None

# Move the robot in a direction
def move_robot(map, robot_pos, direction):
    dir_vectors = {
        "^" : [0, -1],
        "v" : [0, 1],
        "<" : [-1, 0],
        ">" : [1, 0]
    }
    dir_vector = dir_vectors[direction]

    # Scan in a direction
    pos = list(robot_pos)
    while True:
        pos = [sum(i) for i in zip(pos, dir_vector)]

        # Reached a wall, can't move
        if map[pos[1]][pos[0]] == "#":
            return robot_pos
        
        # Make sure to check the second side of double-width boxes for moving up/down
        if direction == "^":
            if (map[pos[1]][pos[0]] == "[") and (map[pos[1]-1][pos[0]+1] == "#"): return robot_pos
            if (map[pos[1]][pos[0]] == "]") and (map[pos[1]-1][pos[0]-1] == "#"): return robot_pos
        if direction == "v":
            if (map[pos[1]][pos[0]] == "[") and (map[pos[1]+1][pos[0]+1] == "#"): return robot_pos
            if (map[pos[1]][pos[0]] == "]") and (map[pos[1]-1][pos[0]+1] == "#"): return robot_pos
        
        # Reached an empty spot, slide previous positions over
        if map[pos[1]][pos[0]] == ".":
            while True:
                prev_pos = [i - j for i, j in zip(pos, dir_vector)]
                map[pos[1]][pos[0]] = map[prev_pos[1]][prev_pos[0]]
                map[prev_pos[1]][prev_pos[0]] = "."

                if prev_pos == robot_pos:
                    return [sum(i) for i in zip(robot_pos, dir_vector)]
                pos = list(prev_pos)

# Load the input file
with open("input.txt", "r") as filein:
    raw_data = filein.read()
raw_data = raw_data.split("\n\n")
init_map = [[j for j in i] for i in raw_data[0].split("\n")]
mov_data = [i for i in raw_data[1] if i in ["^", "v", "<", ">"]]

map = [[j for j in i] for i in init_map]
robot_pos = locate_robot(map)
for i in mov_data:
    robot_pos = move_robot(map, robot_pos, i)
print(f"Sum of box coordinates: {calc_box_coord_sum(map)}")

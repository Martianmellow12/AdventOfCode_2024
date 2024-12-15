import time

# Print out the map
def print_map(boxes, walls, robot_pos, robot_char="@"):
    width = max([i[0] for i in walls])
    height = max([i[1] for i in walls])
    x = 0
    y = 0
    while y < height+1:
        x = 0
        while x < width+1:
            if [x, y] in walls:
                print("\033[0;34m#\033[0m", end="")
            elif [x, y] in boxes:
                print("\033[0;32m[]\033[0m", end="")
                x += 1
            elif [x, y] == robot_pos:
                print(f"\033[7m\033[1;33m{robot_char}\033[0m", end="")
            else:
                print("\033[1;30m.\033[0m", end="")
            x += 1
        y += 1
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

# Convert all boxes to a set of coordinates (left edges)
def boxes_to_coords(map):
    boxes = list()
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "[":
                boxes.append([x, y])
    return boxes

# Convert all walls to a set of coordinates
def walls_to_coords(map):
    walls = list()
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "#":
                walls.append([x, y])
    return walls

# Move a box in a particular direction
def move_box(boxes, box_idx, walls, direction):
    direction_vectors = {
        "^" : [0, -1],
        "v" : [0, 1],
        "<" : [-1, 0],
        ">" : [1, 0]
    }
    dv = direction_vectors[direction]
    moved_boxes = list()

    r_move_box(boxes, box_idx, walls, direction, moved_boxes)
    if -1 in moved_boxes:
        return False
    else:
        for idx in set(moved_boxes):
            boxes[idx] = [sum(i) for i in zip(boxes[idx], dv)]
        return True

def r_move_box(boxes, box_idx, walls, direction, moved_boxes):
    bx, by = boxes[box_idx]

    if direction == "^":
        if ([bx, by-1] in walls) or ([bx+1, by-1] in walls):
            moved_boxes.append(-1)
            return
        if ([bx-1, by-1] in boxes):
            r_move_box(boxes, boxes.index([bx-1, by-1]), walls, direction, moved_boxes)
        if ([bx, by-1] in boxes):
            r_move_box(boxes, boxes.index([bx, by-1]), walls, direction, moved_boxes)
        if ([bx+1, by-1] in boxes):
            r_move_box(boxes, boxes.index([bx+1, by-1]), walls, direction, moved_boxes)
        moved_boxes.append(box_idx)
    
    if direction == "v":
        if ([bx, by+1] in walls) or ([bx+1, by+1] in walls):
            moved_boxes.append(-1)
            return
        if ([bx-1, by+1] in boxes):
            r_move_box(boxes, boxes.index([bx-1, by+1]), walls, direction, moved_boxes)
        if ([bx, by+1] in boxes):
            r_move_box(boxes, boxes.index([bx, by+1]), walls, direction, moved_boxes)
        if ([bx+1, by+1] in boxes):
            r_move_box(boxes, boxes.index([bx+1, by+1]), walls, direction, moved_boxes)
        moved_boxes.append(box_idx)
    
    if direction == "<":
        if [bx-1, by] in walls:
            moved_boxes.append(-1)
            return
        if [bx-2, by] in boxes:
            r_move_box(boxes, boxes.index([bx-2, by]), walls, direction, moved_boxes)
        moved_boxes.append(box_idx)
    
    if direction == ">":
        if [bx+2, by] in walls:
            moved_boxes.append(-1)
            return
        if [bx+2, by] in boxes:
            r_move_box(boxes, boxes.index([bx+2, by]), walls, direction, moved_boxes)
        moved_boxes.append(box_idx)

# Move the robot
def move_robot(boxes, walls, robot_pos, direction):
    rx, ry = robot_pos
    can_move = True

    if direction == "^":
        if [rx, ry-1] in walls: return robot_pos
        if [rx-1, ry-1] in boxes: can_move &= move_box(boxes, boxes.index([rx-1, ry-1]), walls, direction)
        if [rx, ry-1] in boxes: can_move &= move_box(boxes, boxes.index([rx, ry-1]), walls, direction)
        if can_move: return [rx, ry-1]
        else: return robot_pos
        
    if direction == "v":
        if [rx, ry+1] in walls: return robot_pos
        if [rx-1, ry+1] in boxes: can_move &= move_box(boxes, boxes.index([rx-1, ry+1]), walls, direction)
        if [rx, ry+1] in boxes: can_move &= move_box(boxes, boxes.index([rx, ry+1]), walls, direction)
        if can_move: return [rx, ry+1]
        else: return robot_pos

    if direction == "<":
        if [rx-1, ry] in walls: return robot_pos
        if [rx-2, ry] in boxes: can_move &= move_box(boxes, boxes.index([rx-2, ry]), walls, direction)
        if can_move: return [rx-1, ry]
        else: return robot_pos

    if direction == ">":
        if [rx+1, ry] in walls: return robot_pos
        if [rx+1, ry] in boxes: can_move &= move_box(boxes, boxes.index([rx+1, ry]), walls, direction)
        if can_move: return [rx+1, ry]
        else: return robot_pos
        
# Calculate the sum of all box coordinates
def calc_box_coord_sum(boxes):
    coord_sum = 0
    for i in boxes:
        coord_sum += (100*i[1] + i[0])
    return coord_sum

# Locate the robot on the map
def locate_robot(map):
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "@": return [x, y]
    return None

# Load the input file
with open("input.txt", "r") as filein:
    raw_data = filein.read()
raw_data = raw_data.split("\n\n")
init_map = [[j for j in i] for i in raw_data[0].split("\n")]
mov_data = [i for i in raw_data[1] if i in ["^", "v", "<", ">"]]

map = [[j for j in i] for i in init_map]
map = upscale_map(map)
robot_pos = locate_robot(map)
boxes = boxes_to_coords(map)
walls = walls_to_coords(map)

for i in mov_data:
    robot_pos = move_robot(boxes, walls, robot_pos, i)

print(f"Sum of box coordinates: {calc_box_coord_sum(boxes)}")

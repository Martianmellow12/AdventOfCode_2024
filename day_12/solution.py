# Get the number of fences needed for a given location
def num_fences(garden, pos, plant_t):
    garden_w = len(garden[0])
    garden_h = len(garden)
    pos_x = pos[0]
    pos_y = pos[1]

    results = 0
    positions = list()
    if pos_x > 0: positions.append([pos_x-1, pos_y])
    else: results += 1
    if pos_x < (garden_w-1): positions.append([pos_x+1, pos_y])
    else: results += 1
    if pos_y > 0: positions.append([pos_x, pos_y-1])
    else: results += 1
    if pos_y < (garden_h-1): positions.append([pos_x, pos_y+1])
    else: results += 1
    
    for new_pos in positions:
        if garden[new_pos[1]][new_pos[0]] != plant_t: results += 1

    return results

# Get the price of a plot starting at a given position [[area, perim], plot_points]
def get_plot_info(garden, pos):
    visited_good = list()
    visited_bad = list()
    garden_size = [len(garden[0]), len(garden)]
    plant_t = garden[pos[1]][pos[0]]
    info = [0, 0]

    r_get_plot_info(garden, garden_size, pos, plant_t, info, visited_good, visited_bad)
    return [plant_t, info, visited_good, visited_bad]

def r_get_plot_info(garden, garden_size, pos, plant_t, info, visited_good, visited_bad):

    # Add perimiters for edges and other plants
    if (pos[0] < 0) or (pos[0] >= garden_size[0]) or (pos[1] < 0) or (pos[1] >= garden_size[1]) or garden[pos[1]][pos[0]] != plant_t:
        visited_bad.append(pos)
        info[1] += 1
        return
    else:
        visited_good.append(pos)
        info[0] += 1

    # Get info from surrounding plots
    plots = [
        [pos[0]+1, pos[1]],
        [pos[0]-1, pos[1]],
        [pos[0], pos[1]+1],
        [pos[0], pos[1]-1]
    ]
    for i in plots:
        if i in visited_bad:
            info[1] += 1
        elif i not in visited_good:
            r_get_plot_info(garden, garden_size, i, plant_t, info, visited_good, visited_bad)
    return

# Check if a point is within the bounds of the garden
def in_bounds(garden, point):
    x, y = point
    garden_w, garden_h = [len(garden[0]), len(garden)]
    if (x < 0) or (x >= garden_w): return False
    if (y < 0) or (y >= garden_h): return False
    return True

# Check if a point contains a type of plant
def is_plant(garden, point, plant_t):
    if not in_bounds(garden, point): return False
    if garden[point[1]][point[0]] != plant_t: return False
    return True

# Count the number of convex corners for a point
def count_convex_corners(garden, point):
    x, y = point
    plant_t = garden[y][x]

    orth_sides = [
        [[x, y-1], [x+1, y]],
        [[x+1, y], [x, y+1]],
        [[x, y+1], [x-1, y]],
        [[x-1, y], [x, y-1]]
    ]

    # Validate side combinations
    num_corners = 0
    for i in orth_sides:
        if (not is_plant(garden, i[0], plant_t)) and (not is_plant(garden, i[1], plant_t)):
            num_corners += 1
    return num_corners

# Count concave corners
def count_concave_corners(garden, point):
    x, y = point
    plant_t = garden[y][x]

    corners = [
        [x-1, y-1],
        [x+1, y-1],
        [x+1, y+1],
        [x-1, y+1]
    ]

    num_corners = 0
    for c in corners:
        cx, cy = c
        if in_bounds(garden, c) and (not is_plant(garden, c, plant_t)) and is_plant(garden, [cx, y], plant_t) and is_plant(garden, [x, cy], plant_t):
            num_corners += 1
    return num_corners


# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()
garden = [[j for j in i] for i in raw_data.split("\n")]

finished_points = list()
plots = list()
price = 0

for y in range(0, len(garden)):
    for x in range(0, len(garden[y])):
        if [x, y] not in finished_points:
            result = get_plot_info(garden, [x, y])
            plots.append(result)
            finished_points += result[2]
            price += result[1][0]*result[1][1]

print(f"Price (part 1): {price}")


price = 0
for plot in plots:
    num_corners = 0
    for point in plot[2]:
        num_corners += (count_convex_corners(garden, point) + count_concave_corners(garden, point))
    price += plot[1][0]*num_corners

print(f"Price (part 2): {price}")
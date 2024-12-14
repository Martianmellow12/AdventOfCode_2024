# Step all robots
def step_robots(robots, field_size):
    width, height = field_size

    for robot in robots:
        new_x = robot[0][0] + robot[1][0]
        new_y = robot[0][1] + robot[1][1]
        while new_x < 0: new_x += width
        while new_y < 0: new_y += height
        while new_x >= width: new_x -= width
        while new_y >= height: new_y -= height
        robot[0][0] = new_x
        robot[0][1] = new_y

# Get the quadrant of a point
def get_quadrant(point, field_size):
    x, y = point
    mid_x = field_size[0] // 2
    mid_y = field_size[1] // 2
    if (x > mid_x) and (y < mid_y): return 0
    if (x < mid_x) and (y < mid_y): return 1
    if (x < mid_x) and (y > mid_y): return 2
    if (x > mid_x) and (y > mid_y): return 3
    return None

# Calculate the safety factor
def calc_safety_factor(robots, field_size):
    num_robots = [0, 0, 0, 0]
    for i in robots:
        q = get_quadrant(i[0], field_size)
        if q != None:
            num_robots[q] += 1
    result = 1
    for i in num_robots: result *= i
    return result

# Check if any robots overlap
def no_overlaps(robots):
    robot_pos = [i[0] for i in robots]
    for i in robot_pos:
        if robot_pos.count(i) != 1: return False
    return True

# Print the field
def print_field(robots, field_size):
    robot_pos = [i[0] for i in robots]
    for y in range(0, field_size[1]):
        for x in range(0, field_size[0]):
            if [x, y] in robot_pos: print("#", end="")
            else: print(".", end="")
        print("")

# Load the input
with open("input.txt", "r") as filein:
    raw_input = filein.read()
robots = raw_input.split("\n")
for i in range(0, len(robots)):
    robots[i] = robots[i].replace("p=", "").replace("v=", "").split(" ")
    robots[i] = [j.split(",") for j in robots[i]]
    for j in range(0, len(robots[i])):
        robots[i][j] = [int(k) for k in robots[i][j]]

field_size = [101, 103]
iters = 100

counter = 0
for i in range(0, iters):
    counter += 1
    step_robots(robots, field_size)
    if no_overlaps(robots):
        print(counter)
        print_field(robots, field_size)
print(f"Safety factor: {calc_safety_factor(robots, field_size)}")
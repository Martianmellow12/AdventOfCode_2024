# Scale a point
def scale_point(point, scale):
    return [point[0]*scale, point[1]*scale]

# Add a scalar combination of two points
def add_scaled_points(a, a_scale, b, b_scale):
    new_a = scale_point(a, a_scale)
    new_b = scale_point(b, b_scale)
    return [new_a[0]+new_b[0], new_a[1]+new_b[1]]

# Check if a point has passed a target (-1 = no, 0 = at target, 1 = yes)
def passed_target(point, target):
    px, py = point
    tx, ty = target
    if (px == tx) and (py == ty): return 0
    if (px <= tx) and (py <= ty): return -1
    return 1

def solve_eq(point1, point2, target):
    x1, y1 = point1
    x2, y2 = point2
    cx, cy = target
    # Solve for the a scale
    numerator = cx - ((x2/y2) * cy)
    denominator = x1 - ((x2/y2) * y1)
    a_scale = numerator/denominator

    # Solve for the b scale
    numerator = cy - (a_scale*y1)
    denominator = y2
    b_scale = numerator/denominator

    return [round(a_scale), round(b_scale)]

# Load and parse the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()
games = [i.split("\n") for i in raw_data.split("\n\n")]
for i in range(0, len(games)):
    for j in range(0, 3):
        if j == 0:
            tmp = games[i][j].replace("Button A: X+", "").replace(" Y+", "").split(",")
            games[i][j] = [int(num) for num in tmp]
        if j == 1:
            tmp = games[i][j].replace("Button B: X+", "").replace(" Y+", "").split(",")
            games[i][j] = [int(num) for num in tmp]
        if j == 2:
            tmp = games[i][j].replace("Prize: X=", "").replace(" Y=", "").split(",")
            games[i][j] = [int(num) for num in tmp]


# Calculate matches for all games
costs = list()
for game in games:
    a = game[0]
    b = game[1]
    t = [game[2][0]+10000000000000, game[2][1]+10000000000000]
    tokens = solve_eq(a, b, t)
    cost = 3*tokens[0] + tokens[1]

    if (add_scaled_points(a, tokens[0], b, tokens[1]) == t):
        costs.append(cost)

print(f"Minimum cost: {sum(costs)}")
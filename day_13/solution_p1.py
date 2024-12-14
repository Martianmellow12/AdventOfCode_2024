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
matches = list()
for game in games:
    a = game[0]
    b = game[1]
    t = game[2]
    a_scale = 0
    b_scale = 0
    local_matches = list()

    # Find an initial scalar past the target, then adjust it to our starting point
    while passed_target(scale_point(a, a_scale), t) <= 0:
        a_scale += 1
    a_scale -= 1
    
    while a_scale >= 0:
        if passed_target(add_scaled_points(a, a_scale, b, b_scale), t) == 0:
            local_matches.append([a_scale, b_scale])

        while passed_target(add_scaled_points(a, a_scale, b, b_scale), t) < 0:
            b_scale += 1
        if passed_target(add_scaled_points(a, a_scale, b, b_scale), t) == 0:
            local_matches.append([a_scale, b_scale])

        a_scale -= 1
        b_scale = 0
    matches.append(local_matches)

# Calculate minimum cost
min_cost = 0
for game in matches:
    costs = list()
    for i in game:
        costs.append(3*i[0] + i[1])
    if len(costs) > 0: min_cost += min(costs)

print(f"Minimum cost: {min_cost}")
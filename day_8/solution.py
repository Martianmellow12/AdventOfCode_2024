# Calculate antinodes given two stations
def calc_antinodes(stat1, stat2, bound=1):
    antinodes = list()
    diff = [stat2[0] - stat1[0], stat2[1] - stat1[1]]

    for i in range(1, bound+1):
        stat1_antinode = [stat1[0] - (diff[0]*i), stat1[1] - (diff[1]*i)]
        stat2_antinode = [stat2[0] + (diff[0]*i), stat2[1] + (diff[1]*i)]
        antinodes += [stat1_antinode, stat2_antinode]

    return antinodes

# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()
init_input = raw_data.split("\n")
for i in range(0, len(init_input)):
    init_input[i] = [j for j in init_input[i]]
input_w = len(init_input[0])
input_h = len(init_input)

# Create a map of all antenna
ant_map = dict()
for y in range(0, len(init_input)):
    for x in range(0, len(init_input[y])):
        loc = init_input[y][x]
        if loc == ".": continue
        if loc not in ant_map.keys(): ant_map[loc] = list()
        ant_map[loc].append([x, y])


################
#    PART 1    #
################

# Calculate all antinodes
antinode_map = dict()
for i in ant_map.keys(): antinode_map[i] = list()
for key in ant_map.keys():
    for i in range(0, len(ant_map[key])):
        for j in ant_map[key][i+1:]:
            antinodes = calc_antinodes(ant_map[key][i], j)
            for k in antinodes:
                if k in antinode_map[key]: continue
                if (k[0] < 0) or (k[0] >= input_w) or (k[1] < 0) or (k[1] >= input_h): continue
                antinode_map[key].append(k)
            
# Sum up the antinodes
unique_antinodes = list()
for key in antinode_map.keys():
    for i in antinode_map[key]:
        if i not in unique_antinodes:
            unique_antinodes.append(i)

print(f"Unique antinodes: {len(unique_antinodes)}")


##############
#   PART 2   #
##############

# Calculate all antinodes
antinode_map = dict()
for i in ant_map.keys(): antinode_map[i] = list()
for key in ant_map.keys():
    for i in range(0, len(ant_map[key])):
        for j in ant_map[key][i+1:]:
            antinodes = calc_antinodes(ant_map[key][i], j, bound=10000)
            for k in antinodes:
                if k in antinode_map[key]: continue
                if (k[0] < 0) or (k[0] >= input_w) or (k[1] < 0) or (k[1] >= input_h): continue
                antinode_map[key].append(k)
            
# Sum up the antinodes
unique_antinodes = list()
for key in antinode_map.keys():
    for i in antinode_map[key]:
        if i not in unique_antinodes:
            unique_antinodes.append(i)

# Include any antennas that weren't already counted as antinodes
for key in ant_map:
    for i in ant_map[key]:
        if i not in unique_antinodes:
            unique_antinodes.append(i)

print(f"Unique antinodes (part 2): {len(unique_antinodes)}")

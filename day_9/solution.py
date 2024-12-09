# Convert a disk map string to a list
def disk_map_str_to_list(disk_map):
    result = list()
    for i in range(0, len(disk_map)):
        if (i % 2) == 0: result += [str(i // 2)]*int(disk_map[i])
        else: result += ["."]*int(disk_map[i])
    return result

# Compress a disk map
def compress_disk_map(disk_map):
    num_blocks = len(disk_map) - disk_map.count(".")
    left_idx = 0
    right_idx = len(disk_map) - 1

    while True:
        # Find an empty slot
        while disk_map[left_idx] != ".":
            left_idx += 1

        if left_idx >= num_blocks: break

        # Find an item to fill it
        while disk_map[right_idx] == ".":
            right_idx -= 1

        disk_map[left_idx] = disk_map[right_idx]
        disk_map[right_idx] = "."

    return disk_map

# Compress a disk map (for part 2 solution)
def compress_disk_map_p2(disk_map):
    # Create a list of all empty space sizes and their starting indices
    empty_spaces = list()
    space_size = 0
    for idx, i in enumerate(disk_map):
        if i == ".":
            space_size += 1
        elif i !="." and space_size > 0:
            empty_spaces.append([space_size, idx - space_size])
            space_size = 0
    if space_size > 0:
        empty_spaces.append([space_size, idx + 1 - space_size])

    # Create a list of all file sizes and their starting indices
    files = list()
    file_size = 0
    file_id = None
    for idx, i in enumerate(disk_map):
        if i != ".":
            if (i != file_id) and (file_size > 0):
                files.append([file_size, idx - file_size, file_id])
                file_size = 0
            file_id = i
            file_size += 1
        elif i == "." and file_size > 0:
            files.append([file_size, idx - file_size, file_id])
            file_size = 0
            file_id = None
    if file_size > 0:
        files.append([file_size, idx + 1 - file_size, file_id])
    
    # Search for free space for each file
    files.reverse()
    print(files[0:2])
    for file in files:
        for space in empty_spaces:
            # Copy the file if it fits into a space
            if (file[0] <= space[0]) and (file[1] > space[1]):
                # Copy
                for i in range(0, file[0]):
                    disk_map[space[1] + i] = file[2]
                    disk_map[file[1] + i] = "."
                
                # Update tracking
                space[0] -= file[0]
                space[1] += file[0]

                break

    return disk_map

# Calculate the checksum for a given disk_map_str
def calc_checksum(disk_map):
    checksum = 0
    for idx, i in enumerate(disk_map):
        if i != ".": checksum += idx * int(i)
    return checksum

# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()


##############
#   PART 1   #
##############

# Compress and generate the checksum
disk_map = disk_map_str_to_list(raw_data)
disk_map = compress_disk_map(disk_map)

print(f"Checksum: {calc_checksum(disk_map)}")


##############
#   PART 2   #
##############

# Compress and generate the checksum
disk_map = disk_map_str_to_list(raw_data)
disk_map = compress_disk_map_p2(disk_map)

print(f"Checksum: {calc_checksum(disk_map)}")
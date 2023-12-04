schematic = []
with open('day3/input.txt', 'r') as file:
    file_lines = file.readlines()
    for line in file_lines:
        schematic.append(line.replace('\n', ''))

len_schematic_row = len(schematic[0])
len_schematic_col = len(schematic)

def get_adjacent_num_locations(x, y):
    adjacent_locations = []
    if x > 0:
        # top left
        if y > 0:
            test_value = schematic[x-1][y-1]
            if test_value.isdigit():
                adjacent_locations.append((x-1, y-1))
        # top
        test_value = schematic[x-1][y]
        if test_value.isdigit():
            adjacent_locations.append((x-1, y))

        # top_right
        if y < len_schematic_row-1:
            test_value = schematic[x-1][y+1]
            if test_value.isdigit():
                adjacent_locations.append((x-1, y+1))
    # left
    if y > 0:
        test_value = schematic[x][y-1]
        if test_value.isdigit():
            adjacent_locations.append((x, y-1))

    # right
    if y < len_schematic_row-1:
        test_value = schematic[x][y+1]
        if test_value.isdigit():
            adjacent_locations.append((x, y+1))
    # bottom_left
    if x < len_schematic_col - 1:
        if y > 0:
            test_value = schematic[x+1][y-1]
            if test_value.isdigit():
                adjacent_locations.append((x+1, y-1))
        # bottom
        test_value = schematic[x+1][y]
        if test_value.isdigit():
            adjacent_locations.append((x+1, y))
        # bottom_right
        if y < len_schematic_row-1:
            test_value = schematic[x+1][y+1]
            if test_value.isdigit():
                adjacent_locations.append((x+1, y+1))

    return adjacent_locations



# def get_part_num_locations(schematic):
#     sum_part_nums = 0
#     for xidx, x in enumerate(schematic):
#         currently_in_number = False
#         current_num_has_symbol = False
#         current_num_in = ''
#         for yidx, y in enumerate(x):
#             if y.isdigit():
#                 currently_in_number = True
#                 current_num_in += y
#                 if not current_num_has_symbol:
#                     if has_symbol_adjacent(xidx, yidx):
#                         current_num_has_symbol = True
#                 if yidx == len(x) - 1:
#                     if current_num_has_symbol:
#                         sum_part_nums += int(current_num_in)
#             else:
#                 if currently_in_number:
#                     if current_num_has_symbol:
#                         sum_part_nums += int(current_num_in)
#                 currently_in_number = False
#                 current_num_in = ''
#                 current_num_has_symbol = False
#                 continue

#     return sum_part_nums


def get_adjacent_num_sum(xidx, yidx):
    print(xidx, yidx)
    row = schematic[xidx]
    current_yidx = yidx
    current_part_num =''
    while row[current_yidx].isdigit():
        current_part_num += schematic[xidx][current_yidx]
        current_yidx+=1
    current_left_yidx = yidx-1
    while row[current_left_yidx].isdigit():
        current_part_num = schematic[xidx][current_left_yidx] + current_part_num
        current_left_yidx-=1
    
    return int(current_part_num)





def get_gear_part_sum(schematic):
    sum_gear_part_nums = 0
    for xidx, x in enumerate(schematic):
        currently_in_number = False
        current_num_has_symbol = False
        current_num_in = ''
        for yidx, y in enumerate(x):
            if y=='*':
                adjacent_num_locations = get_adjacent_num_locations(xidx, yidx)
                if len(adjacent_num_locations) == 2:
                    sum_gear_part_nums += get_adjacent_num_sum(adjacent_num_locations[0][0], adjacent_num_locations[0][1]) + get_adjacent_num_sum(adjacent_num_locations[1][0], adjacent_num_locations[1][1])
    
    return sum_gear_part_nums

    
print(get_gear_part_sum(schematic))

# for part_position in part_positions:
#     x = part_position[0]
#     y = part_position[1]





# is_top_row = False
# is_bottom_row = False
# is_left = False
# is_right = False
# for x in schematic:
#     for y in x:
#         if x == 0:
#             is_top_row = True
#         if x == len(schematic) - 1:
#             is_bottom_row = True
#         if y == 0:
#             is_left = True
#         if y == len(x) - 1:
#             is_right = True



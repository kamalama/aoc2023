schematic = []
with open('day3/input.txt', 'r') as file:
    file_lines = file.readlines()
    for line in file_lines:
        schematic.append(line.replace('\n', ''))

len_schematic_row = len(schematic[0])
len_schematic_col = len(schematic)

def has_symbol_adjacent(x, y):
    # top_left
    if x > 0:
        if y > 0:
            test_value = schematic[x-1][y-1]
            if test_value != '.' and not test_value.isdigit():
                return True
        # top
        test_value = schematic[x-1][y]
        if test_value != '.' and not test_value.isdigit():
            return True

        # top_right
        if y < len_schematic_row-1:
            test_value = schematic[x-1][y+1]
            if test_value != '.' and not test_value.isdigit():
                return True
    # left
    if y > 0:
        test_value = schematic[x][y-1]
        if test_value != '.' and not test_value.isdigit():
            return True

    # right
    if y < len_schematic_row-1:
        test_value = schematic[x][y+1]
        if test_value != '.' and not test_value.isdigit():
            return True
    # bottom_left
    if x < len_schematic_col - 1:
        if y > 0:
            test_value = schematic[x+1][y-1]
            if test_value != '.' and not test_value.isdigit():
                return True
        # bottom
        test_value = schematic[x+1][y]
        if test_value != '.' and not test_value.isdigit():
            return True
        # bottom_right
        if y < len_schematic_row-1:
            test_value = schematic[x+1][y+1]
            if test_value != '.' and not test_value.isdigit():
                return True

    return False



def get_part_num_locations(schematic):
    sum_part_nums = 0
    for xidx, x in enumerate(schematic):
        currently_in_number = False
        current_num_has_symbol = False
        current_num_in = ''
        for yidx, y in enumerate(x):
            if yidx == len(x)-4:
                print('here')
            if y.isdigit():
                currently_in_number = True
                current_num_in += y
                if not current_num_has_symbol:
                    if has_symbol_adjacent(xidx, yidx):
                        current_num_has_symbol = True
                if yidx == len(x) - 1:
                    if current_num_has_symbol:
                        sum_part_nums += int(current_num_in)
            else:
                if currently_in_number:
                    if current_num_has_symbol:
                        sum_part_nums += int(current_num_in)
                currently_in_number = False
                current_num_in = ''
                current_num_has_symbol = False
                continue

    return sum_part_nums

    



    
print(get_part_num_locations(schematic))

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



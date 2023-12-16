schematic = []
with open('day3/input.txt', 'r') as file:
    file_lines = file.readlines()
    for line in file_lines:
        schematic.append(line.replace('\n', ''))

len_schematic_row = len(schematic[0])
len_schematic_col = len(schematic)

def get_adjacent_num_locations(x, y):
    adjacent_part_nums = []
    if x > 0:
        # top left
        if y > 0:
            test_value = schematic[x-1][y-1]
            if test_value.isdigit():
                adjacent_part_num = get_adjacent_num_sum(x-1, y-1)
                if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                    adjacent_part_nums.append(adjacent_part_num)
        # top
        test_value = schematic[x-1][y]
        if test_value.isdigit():
            adjacent_part_num = get_adjacent_num_sum(x-1, y)
            if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                adjacent_part_nums.append(adjacent_part_num)

        # top_right
        if y < len_schematic_row-1:
            test_value = schematic[x-1][y+1]
            if test_value.isdigit():
                adjacent_part_num = get_adjacent_num_sum(x-1, y+1)
                if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                    adjacent_part_nums.append(adjacent_part_num)
    # left
    if y > 0:
        test_value = schematic[x][y-1]
        if test_value.isdigit():
            adjacent_part_num = get_adjacent_num_sum(x, y-1)
            if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                adjacent_part_nums.append(adjacent_part_num)

    # right
    if y < len_schematic_row-1:
        test_value = schematic[x][y+1]
        if test_value.isdigit():
            adjacent_part_num = get_adjacent_num_sum(x, y+1)
            if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                adjacent_part_nums.append(adjacent_part_num)
    # bottom_left
    if x < len_schematic_col - 1:
        if y > 0:
            test_value = schematic[x+1][y-1]
            if test_value.isdigit():
                adjacent_part_num = get_adjacent_num_sum(x+1, y-1)
                if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                    adjacent_part_nums.append(adjacent_part_num)
        # bottom
        test_value = schematic[x+1][y]
        if test_value.isdigit():
            adjacent_part_num = get_adjacent_num_sum(x+1, y)
            if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                adjacent_part_nums.append(adjacent_part_num)
        # bottom_right
        if y < len_schematic_row-1:
            test_value = schematic[x+1][y+1]
            if test_value.isdigit():
                adjacent_part_num = get_adjacent_num_sum(x+1, y+1)
                if len(adjacent_part_nums) == 0 or adjacent_part_num != adjacent_part_nums[-1]:
                    adjacent_part_nums.append(adjacent_part_num)

    return adjacent_part_nums


def get_adjacent_num_sum(xidx, yidx):
    print(xidx, yidx)
    row = schematic[xidx]
    current_yidx = yidx
    current_part_num =''
    print(f'whats the current yidx, xidx and length {yidx}, {xidx}, {len(schematic[xidx])}')
    if current_yidx <140:
        while row[current_yidx].isdigit():
            current_part_num += schematic[xidx][current_yidx]
            if current_yidx == 139:
                break
            else:
                current_yidx+=1
    current_left_yidx = yidx-1
    if current_left_yidx >= 0:
        while row[current_left_yidx].isdigit():
            current_part_num = schematic[xidx][current_left_yidx] + current_part_num
            current_left_yidx-=1
            if current_left_yidx < 0:
                break
    print(f'current part num is {current_part_num}')
    
    return int(current_part_num)





def get_gear_part_sum(schematic):
    sum_gear_part_nums = 0
    for xidx, x in enumerate(schematic):
        for yidx, y in enumerate(x):
            if y=='*':
                adjacent_part_nums = get_adjacent_num_locations(xidx, yidx)
                print(f'the adjacent_part_nums_are {adjacent_part_nums}')
                if len(adjacent_part_nums) != 2:
                    print('stop!')
                else:
                    sum_gear_part_nums = sum_gear_part_nums + (adjacent_part_nums[0] * adjacent_part_nums[1])
                    print(sum_gear_part_nums)
    
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



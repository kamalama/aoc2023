schematic = []
with open('day3/input.txt', 'r') as file:
    file_lines = file.readlines()
    for line in file_lines:
        schematic.append(line.replace('\n', ''))

def find_part_num(x, y):
    part_nums = []
    # top_left
    try:
        int(schematic[x-1][y-1])
        return (x-1, y-1)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # top
    try:
        int(schematic[x-1][y])
        return (x-1,y)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # top_right
    try:
        int(schematic[x-1][y+1])
        return (x-1,y+1)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # left
    try:
        int(schematic[x][y-1])
        return (x,y-1)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # right
    try:
        int(schematic[x][y+1])
        return (x,y+1)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # bottom_left
    try:
        int(schematic[x+1][y-1])
        return (x+1,y-1)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # bottom
    try:
        int(schematic[x+1][y])
        return (x+1,y)
    except:
        print('either that index doesnt work, or inting the character didnt work')
    # bottom_right
    try:
        int(schematic[x+1][y+1])
        return (x+1,y+1)
    except:
        print('either that index doesnt work, or inting the character didnt work')



def get_sum_part_nums(schematic):
    part_positions = []
    for xidx, x in enumerate(schematic):
        for yidx, y in enumerate(x):
            if y == '.':
                continue
            else:
                try:
                    int(y)
                    continue
                except:
                    part_num_location = find_part_num(xidx, yidx)
                    print(part_num_location)
    

def get_full_num(x, y):
    num_str = schematic[x][y]
    for char in schematic[x][y+1:]:
        try:
            int(char)
            num_str += char
        except:
            break
    for char in schematic[x][:y].reverse():
        try:
            int(char)
            num_str = char + num_str
        except:
            break
    print(num_str)
    return int(num_str)



    
print(get_sum_part_nums(schematic))

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



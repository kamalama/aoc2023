
total_allowed = {
    'red': 12,
    'blue': 14,
    'green': 13}

def make_reveal_dict(color_reveal):
    color_reveal_dict = {}
    for color in color_reveal:
        number_and_color = color.split(' ')
        color_reveal_dict[number_and_color[1]] = int(number_and_color[0])
    return color_reveal_dict

with open('day2/input.txt', 'r') as file:
    inputLines = file.readlines()
    total_sum = 0
    for line in inputLines:
        is_not_allowed = False
        clean_line = line.replace('\n', '')
        index_of_colon = clean_line.find(':')
        id = int(clean_line[5:index_of_colon])
        reveals = clean_line[index_of_colon + 2:].split('; ')
        color_reveals = [reveal.split(', ') for reveal in reveals]
        for color_reveal in color_reveals:
            color_reveal_dict = make_reveal_dict(color_reveal)
            for color, count in color_reveal_dict.items():
                if count > total_allowed[color]:
                    is_not_allowed = True
                    break

            if is_not_allowed == True:
                break
        
        if is_not_allowed:
            print(f'is not allowed {color_reveals}')
            continue
        else:
            print(f'adding id because it works {color_reveals}')
            total_sum += id
    
    print(total_sum)
        
                



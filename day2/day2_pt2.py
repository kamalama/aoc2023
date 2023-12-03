
total_allowed = {
    'red': 12,
    'blue': 14,
    'green': 13}

def get_power_value(reveals_split_by_color):
    color_reveal_dict = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for reveal in reveals_split_by_color:
        for color_count in reveal:
            count, color = color_count.split(' ')
            if color_reveal_dict[color] < int(count):
                color_reveal_dict[color] = int(count)
    
    return color_reveal_dict['red'] * color_reveal_dict['blue'] * color_reveal_dict['green']
    


with open('day2/input.txt', 'r') as file:
    inputLines = file.readlines()
    total_powers = 0
    for line in inputLines:
        game = line.replace('\n', '')
        index_of_colon = game.find(':')
        reveals = game[index_of_colon + 2:].split('; ')
        reveals_split_by_color = [reveal.split(', ') for reveal in reveals]
        total_powers += get_power_value(reveals_split_by_color)
    
    print(total_powers)
        
    
        
                



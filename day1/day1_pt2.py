
num_to_word_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

list_of_string_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_string_num_locations(line):
    string_num_locations = []
    for idx, string_num in enumerate(list_of_string_nums):
        operate_line = line
        end_index = 0
        while len(operate_line) >= 3:
            string_location = operate_line.find(string_num)
            if string_location != -1:
                string_num_locations.append([string_num, string_location + end_index, string_location + len(string_num) - 1 + end_index])
                operate_line = operate_line[string_location + len(string_num) - 1:]
                end_index += string_location + len(string_num) - 1
            else:
                break
                
    
    print(f'string_num_locations is {string_num_locations}')
    
    return string_num_locations

def getFirstDigit(line):
    for char in line:
        try:
            int_char = int(char)
            return int_char
        except:
            continue
    return None
    
def getSecondDigit(line):
    for char in reversed(line):
        try:
            int_char = int(char)
            return int_char
        except:
            continue
    return None

def get_lowest_string_num_location(string_num_locations, line):
    lowest_string_num_location = [None, len(line)-1]
    for string_num_location in string_num_locations:
        if string_num_location[1] < lowest_string_num_location[1]:
            lowest_string_num_location = [string_num_location[0], string_num_location[1]]

    return lowest_string_num_location

def get_highest_string_num_location(string_num_locations, line):
    highest_string_num_location = [None, 0]
    for string_num_location in string_num_locations:
        if string_num_location[2] > highest_string_num_location[1]:
            highest_string_num_location = [string_num_location[0], string_num_location[2]]

    return highest_string_num_location

total = 0
with open('day1/input.txt', 'r') as file:
    inputLines = file.readlines()
    for line in inputLines:
        print(f'total is {total}')
        print(f'line is {line}')
        string_num_locations = get_string_num_locations(line)
        if len(string_num_locations) == 0:
            firstDigit = getFirstDigit(line)
            secondDigit = getSecondDigit(line)
        else:  
            lowest_string_num_location = get_lowest_string_num_location(string_num_locations, line)
            highest_string_num_location = get_highest_string_num_location(string_num_locations, line)
            firstDigit = getFirstDigit(line[:lowest_string_num_location[1]])
            secondDigit = getSecondDigit(line[highest_string_num_location[1]:])
            print(f'lowest_string_num_location is {lowest_string_num_location}, highest_string_num_location is {highest_string_num_location}, firstDigit is {firstDigit} and secondDigit is {secondDigit}')
        if not firstDigit:
            firstDigit = num_to_word_map[lowest_string_num_location[0]]
        if not secondDigit:
            secondDigit = num_to_word_map[highest_string_num_location[0]]
        
        total += (10 * firstDigit) + secondDigit
        print(f'expected addition is {(10 * firstDigit) + secondDigit}')
print(f'final total is {total}')


with open('day2/input.txt', 'r') as file:
    inputLines = file.readlines()
    for line in inputLines:
        index_of_colon = line.find(':')
        id = line[5:index_of_colon]

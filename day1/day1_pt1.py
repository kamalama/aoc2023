


def getFirstDigit(line):
    for char in line:
        print(f'char is {char}')
        try:
            int_char = int(char)
            return int_char
        except:
            continue
    
def getSecondDigit(line):
    for char in reversed(line):
        print(f'reverseChar is {char}')

        try:
            int_char = int(char)
            return int_char
        except:
            continue



total = 0
with open('day1/input.txt', 'r') as file:
    inputLines = file.readlines()
    for line in inputLines:
        print(f'total is {total}')
        firstDigit = getFirstDigit(line)
        secondDigit = getSecondDigit(line)
        print(f'firstDigit is {firstDigit}')
        print(f'secondDigit is {secondDigit}')
        total += (10 * firstDigit) + secondDigit
        print(f'new total after firstDigit is {total}')
print(f'final total is {total}')
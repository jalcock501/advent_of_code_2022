'''
Day_06 Part_01 of Advent of code 2022
'''

file_name = 'day_6/input.txt'

def find_marker(data:list[str], num: int) -> int:
    '''
    Finds Marker Number
    Parameters:
        data: list of strings to decipher
    
    Returns:
        int: number from deciphered string
    '''
    for i in range(len(data[0])):
        chunk = set(data[0][i:i + num])
        if len(chunk) == num:
            return i + num

if __name__ == '__main__':
    with open(file_name, 'r') as input_file:
        lines = input_file.read().splitlines()

    print(find_marker(lines,4)) # Part 1
    print(find_marker(lines,14)) # Part 2 
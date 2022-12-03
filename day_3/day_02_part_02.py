'''
Day_03 Part_01 of Advent of code 2022
'''
import string
from day_01_part_01 import get_value

file_name = "day_3/input.txt"

def part_02(lines: list) -> int:
    ''' 
    Solution Part 02 

    Parameters: lines -- list

    Returns: value -- int
    '''
    value = 0
    chunks = [' '.join(lines[i:i+3]).replace('\n', '') for i in range(0, len(lines), 3)]
    for i in chunks:
        group = i.split()
        if len(group) != 3:
            continue
        else:
            match = list(set.intersection(*map(set, group)))[0]
            value += get_value(match)
    
    return value


if __name__ == '__main__':

    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()
        print(part_02(lines))


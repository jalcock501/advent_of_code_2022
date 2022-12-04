'''
Day_03 Part_01 of Advent of code 2022
'''
import string

file_name = "day_3/input.txt"

def get_value(letter:str) -> int:
    ''' 
    Gets value of letter a-z:1-26 A-Z:27-52  

    Parameters: letter -- string

    Returns: value -- int
    '''
    lowercase = {letter: i+1 for i, letter in enumerate(string.ascii_lowercase)}
    uppercase = {letter: i+27 for i, letter in enumerate(string.ascii_uppercase)}
    if letter in uppercase.keys():
        return uppercase[letter]
    else: return lowercase[letter]

def part_01(lines:list) -> int:
    ''' 
    Solution Part 01 

    Parameters: lines -- list

    Returns: value -- int
    '''
    value = 0
    for line in lines:
        compartment_1, compartment_2 = line[:len(line)//2], line[len(line)//2:]
        matches = list(set(compartment_1).intersection(compartment_2))[0]  
        for i in matches:
            value += get_value(i)
    return value


if __name__ == '__main__':

    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()
        print(part_01(lines))


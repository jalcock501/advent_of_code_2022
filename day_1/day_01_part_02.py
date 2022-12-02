''' 
Day_01 Part_02 from advent of code 2022
'''
from day_01_part_01 import *

if __name__ == '__main__':
    file_name = 'input.txt'
    calories = 0

    elf_dict = calculate_calories(create_elf_dict(input_file=file_name))
    for i in find_most_calories(cal_dict=elf_dict, number=3):
        calories += i[1]

    print(elf_dict)
    print(calories)


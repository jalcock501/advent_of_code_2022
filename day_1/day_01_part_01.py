'''
Day_01 Part_01 from the adventofcode_2022
'''

import heapq

def create_elf_dict(input_file: str) -> dict:
    '''
    Returns dictionary of elves (key) and list of calories (value)

    Parameters:
        input_file -- file_name string

    Returns:
        elves_calories -- dict of lists
    '''
    elves_calories = {} # dictionary of elves and calories
    with open(input_file, 'r') as input_data:
        lines = input_data.readlines()
        elf_count = 1  # start count at 1
        elf_calories = []
        for line in lines:  # iterate over lines in file
            if line in ['\n', '\r\n']: # if blank line new elf and empty list
                elf_count += 1
                elf_calories = []
            else:
                elf_calories.append(int(line.strip('\n'))) # strip \n and cast to integer

            elves_calories[f'elf_{elf_count}'] = elf_calories  # create or update dictionary with elf and calories
        
    return elves_calories
        
def calculate_calories(cal_dict: dict) -> dict:
    '''
    Adds all ints in list from dict and returns dict with sum

    Parameters:
        cal_dict -- dict of lists containing ints

    Returns:
        cal_dict -- dict of ints
    '''
    for k,v in cal_dict.items():
        cal_dict[k] = sum(v) # adds all elements of list together
    return cal_dict 

def find_most_calories(cal_dict: dict, number: int) -> list[tuple]:
    '''
    Returns N largest values from dictionary

    Parameters:
        cal_dict -- dictionary of ints

    Returns:
        list of tuples
    '''
    return heapq.nlargest(number, cal_dict.items(), key=lambda i: i[1])

if __name__ == '__main__':

    file_name = "input.txt"
    elf_dict = calculate_calories(create_elf_dict(input_file=file_name))
    calories_dense_elf = find_most_calories(cal_dict=elf_dict, number=1)
    print(f"The elf carring the most calories is {calories_dense_elf[0][0]} with a total of {calories_dense_elf[0][1]} cals")

        

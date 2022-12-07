'''
Day_07 Part_01 of Advent of code 2022
'''
from collections import defaultdict

__file_name = 'day_7/input.txt'
small_directories = 100000
small_dir_total = 0
device_memory = 70000000
update_size = 30000000

def command_file_parser(data: list[str]) -> dict:
    '''
    Parses Input data to create list of Files 
    Parameters:
        data: list of string input data
    Returns:
        dirs: dict of directories and sizes
    '''
    dirs = defaultdict(int)
    location = []
    for line in lines:
        splitter = line.split()
        if splitter[0] == '$':
            _dir = ''
            if splitter[1] == 'cd' and '..' in splitter[2]:
                location.pop()
            elif splitter[1] == 'cd':
                location.append(splitter[2])
        elif splitter[0].isnumeric():
            for parent_dir in range(len(location)):
                dirs["".join(location[:parent_dir+1])] += int(splitter[0])

    return dirs


if __name__ == '__main__':
    with open(__file_name, 'r') as input_file:
        lines = input_file.read().splitlines()

    dir_sizes = command_file_parser(lines)

    parent_dirs = []
    for dirs, size in dir_sizes.items():
        if size < small_directories:
            small_dir_total += size
        if (dir_sizes['/'] - size) <= (device_memory - update_size):
            parent_dirs.append(size)
        
    parent_dirs = sorted(parent_dirs)

    print(small_dir_total)
    print(parent_dirs[0])

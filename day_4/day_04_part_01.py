'''
Day_04 Part_01 of Advent of code 2022
'''

file_name = 'day_4/input.txt'

if __name__ == '__main__':
    counter = 0
    overlaps = 0
    with open(file_name, 'r') as input_file:
        for line in input_file.readlines():
            elf1, elf2 = line.strip('\n').split(',')
            elf1_range = range(int(elf1.split('-')[0]), int(elf1.split('-')[-1])+1)
            elf2_range = range(int(elf2.split('-')[0]), int(elf2.split('-')[-1])+1)

            if (elf1_range.start <= elf2_range.start and elf2_range.stop <= elf1_range.stop)\
            or (elf2_range.start <= elf1_range.start) and (elf1_range.stop <= elf2_range.stop):
                counter += 1
            
            if set(elf1_range).intersection(elf2_range):
                overlaps += 1
            
    print(counter)
    print(overlaps)
            
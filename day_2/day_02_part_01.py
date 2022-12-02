'''
Day_02 Part_01 of Advent of code 2022
'''

win = 6
draw = 3
loss = 0

def win_loss(opponent, me):
    if opponent == 'A':
        if me == 'X': return draw + 1
        elif me == 'Y': return win + 2
        else: return loss + 3
    elif opponent == 'B':
        if me == 'X': return loss + 1
        elif me == 'Y': return draw + 2
        else: return win + 3
    else:
        if me == 'X': return win + 1
        elif me == 'Y': return loss + 2
        else: return draw + 3


if __name__ == '__main__':
    file_name = 'day_2/input.txt'
    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()

    score = 0
    for line in lines:
        opponent, me = line.split()
        score += win_loss(opponent, me) 
    
    print(score)
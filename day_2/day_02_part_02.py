'''
Day_02 Part_01 of Advent of code 2022
'''

game = {
    # OPPONENT - SCORE - LOSS - WIN
    "A": [1, "C", "B"],
    "B": [2, "A", "C"],
    "C": [3, "B", "A"],
    # OUTCOME SCORES
    "X": 0,
    "Y": 3,
    "Z": 6,
}

def win_loss(opponent, me):
    shape = game.get(opponent)
    outcome = game.get(me)

    if me == 'X':
        return (game.get(shape[1])[0] + outcome)
    elif me == 'Y':
        return shape[0] + outcome
    else:
        return game.get(shape[2])[0] + outcome
    
if __name__ == '__main__':
    file_name = 'day_2/input.txt'
    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()

    score = 0
    for line in lines:
        opponent, me = line.split()
        print(win_loss(opponent,me))
        score += win_loss(opponent, me) 
    
    print(score)    
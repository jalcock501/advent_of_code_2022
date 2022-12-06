'''
Day 5 adevnt of code 2022
'''

file_name = 'day_5/input.txt'

def get_layout_instructions(data: list[str]) -> list[list]:
    ''' 
    Splits list of strings on empty element

    Parameters:
        data: list of strings

    Returns:
        list[list] -- list of lists split on empty elements
    '''
    return [data[: data.index('')], data[data.index('') +1:]]

def read_instructions(instruction: str) -> tuple[int]:
    '''
    Reads in structions and converts them into tuple of ints

    Parameters:
        instructions -- string: string of instructions

    Returns:
        tuple(int) -- returns tuple of ints derived from string
    '''
    amount = loc_from = loc_to = 0
    for idx, i in enumerate(instruction):
        if i == 'move':
            amount = int(instruction[idx+1])
        elif i == 'from':
            loc_from = int(instruction[idx+1])
        elif i == 'to':
            loc_to = int(instruction[idx+1])
        else: continue
    return amount, loc_from, loc_to

def create_table(crate_layout: list) -> dict[list]:
    ''' 
    Create table layout of crates
    
    Parameters:
        crate_layout -- list of strings

    Returns:
        dict of lists
    '''
    stacks = int(crate_layout[-1].split()[-1])
    for idx, i in enumerate(crate_layout):
        crate_layout[idx] = [i[j:j+4] for j in range(0, len(i), 4)]
    crate_layout.pop()
    table = {s: [] for s in range(1, stacks + 1)}
    for stack in reversed(crate_layout):
        for i in range(stacks):
            if '  ' in stack[i]:
                continue
            table[i+1].append(stack[i].strip(' '))
    return table
    
def move_crates(crates: dict[list], amount: int, _from:int, _to:int, mover:int) -> dict[list]:
    '''
    Move Crates to new stack

    Parameters:
        crates: dictionary of lists containing stack info
        amount: int amount of crates to move for this stack
        _from: int from stack A
        _to: int to stack B
        mover: int which mover model number

    Returns:
        crates: dictionary of lists containing stack info
    '''
    if mover == 9000:
        for i in range(amount):
            crates[_to].append(crates[_from][-1])
            del crates[_from][-1]
    
    if mover == 9001:
        moving = []
        for i in range(amount):
            moving.append(crates[_from][-1])
            del crates[_from][-1]
        
        crates[_to].extend(reversed(moving))
        
    return crates

def main(mover:int, data:list):
    '''
    Main function
    Parameters:
        mover: int model of mover
        data: list of input data 

    Returns:
        None
    '''
    crate_layout, instructions = get_layout_instructions(data)
    layout = create_table(crate_layout=crate_layout)
    for instruction in instructions:
        amount, _from, _to = read_instructions(instruction.split(' '))
        crates = move_crates(layout, amount, _from, _to, mover)

    top_stack = ''
    for k, v in crates.items():
        top_stack += v[-1][1]
    print(top_stack)


if __name__ == '__main__':
    with open(file_name, 'r') as input_file:
        lines = input_file.read().splitlines()

    main(mover=9000, lines=lines)
    main(mover=9001, lines=lines)
    
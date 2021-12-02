from auth import getInput

input = getInput(2)

directions = {
    'up': 0,
    'down': 0,
    'forward': {
        'depth': 0,
        'hor': 0
    }
}

for line in input.iter_lines():
    mov = line.decode('ASCII').split()
    if(mov[0] == 'forward'):
        directions['forward']['hor'] += int(mov[1])
        directions['forward']['depth'] += (int(mov[1])
                                           * (directions['down'] - directions['up']))
    else:
        directions[mov[0]] += int(mov[1])

print(directions['forward']['depth']*directions['forward']['hor'])


from auth import getInput
import numpy as np
input = getInput(4).text.strip('\n').split('\n\n')

draws = input[0].split(",")
draws = list(map(int, draws))
w = {}
winningBoard = []
winningLine = []
minVal = 999999999
total = 0

boards = np.array([[list(map(int, i.split())) for i in b.split('\n')]
                   for b in input[1:]])

for i, board in enumerate(boards):
    col = np.array(board).transpose().tolist()
    row = np.array(board).tolist()
    for line in row:
        r = [val for val in draws if val in line]
        if(minVal > draws.index(r[4])):
            minVal = draws.index(r[4])
            winningBoard = board
            winningLine = line

    for line in col:
        r = [val for val in draws if val in line]
        if(minVal > draws.index(r[4])):
            minVal = draws.index(r[4])
            winningBoard = board
            winningLine = line
        if(i in w and w[i] > draws.index(r[4])):
            w[i] = draws.index(r[4])
        else:
            w[i] = draws.index(r[4])


maxVal = max(w, key=w.get)

res = sum([val for line in winningBoard.tolist()
           for val in line if val not in draws[:minVal+1]])*draws[minVal]
res2 = sum([val for line in boards[maxVal].tolist()
           for val in line if val not in draws[:maxVal+1]])*draws[w[maxVal]]
print([val for line in boards[maxVal].tolist() for val in line])

print(res)
print(res2)

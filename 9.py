from auth import getInput
import numpy as np
from collections import Counter
input = getInput(9).text.splitlines()

# input = [[int(num) for num in line] for line in input]
# input = [[int(num) for num in line]
#          for line in "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".splitlines()]
input = [[int(num) for num in line]
         for line in "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".splitlines()]
lows = []
coordinates = []

for i, line in enumerate(input):
    for j, num in enumerate(line):
        if((j == 0 or num < line[j-1]) and (j == len(line) - 1 or num < line[j+1])):
            if((i == 0 or num < input[i-1][j]) and (i == len(input) - 1 or num < input[i+1][j])):
                lows.append(num)
                coordinates.append([j, i])

basinMap = {}
for x, y in coordinates:
    basinMap[(x, y)] = set()

print(basinMap)

# for y, line in enumerate(input):
#     for x, num in enumerate(line):
#         print

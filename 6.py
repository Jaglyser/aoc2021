from auth import getInput
from collections import Counter
from itertools import repeat
from matplotlib import pyplot as plt
from random import randint
fishies = dict(Counter(list(map(int, getInput(6).text.split(",")))))
days = range(256)

for i in range(-1, 9):
    if(i not in fishies):
        fishies[i] = 0

for day in days:
    for i in range(9):
        fishies[i-1] = fishies[i]
    if(-1 in fishies.keys()):
        fishies[8] = fishies[-1]
        fishies[6] += fishies[-1]
        fishies[-1] = 0
totalfish = list(repeat(randint(1, 10), 10))
print(totalfish)

print(sum(fishies.values()))

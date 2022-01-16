from statistics import median
from math import floor
from auth import getInput
list = list(map(int, getInput(7).text.split(",")))
print("part1:", sum([abs(val - median(list)) for val in list]))
print("part2:", sum([sum(val) for val in [[j for j in range(abs(i - int((floor(sum(list)/len(list))))) + 1)]
                                          for i in list]]))

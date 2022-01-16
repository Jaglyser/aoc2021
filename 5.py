from auth import getInput
import numpy as np
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt
coordinates = []
noDiagonal = []
input = [list(map(int, re.split(',| -> ', line)))
         for line in getInput(5).text.splitlines()]

plt.style.use('dark_background')


def numberOfDuplicates():
    d = Counter(coordinates)
    dupes = [val for val in d if d[val] > 1]
    return len(dupes)


def loop(diagonal):
    for cell in input:
        x0, y0, x1, y1 = cell
        plt.plot([x0, x1], [y0, y1])
        dx = 0 if x0 == x1 else 1 if x0 < x1 else -1
        dy = 0 if y0 == y1 else 1 if y0 < y1 else -1
        if(x0 != x1 and y0 != y1 and not diagonal):
            continue
        r = range(abs(x0-x1)+1) if dy == 0 else range(abs(y0-y1) + 1)
        coordinates.extend(
            [(dx*n + x0, dy*n + y0) for n in r])


if __name__ == "__main__":
    loop(False)
    print(numberOfDuplicates())
    # plt.plot([coordinates])
    # plt.show()
    # print(coordinates)
    plt.show()

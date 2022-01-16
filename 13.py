from requests.models import cookiejar_from_dict
from auth import getInput
from matplotlib import pyplot as plt

input = getInput(13).text.splitlines()
folds = input[-12:]
print(folds)
coordinates = [list(map(int, line.split(","))) for line in input[:-13]]
newCo = set()
for x, y in coordinates:
    newCo.add((abs(x - 655), y))

newCo2 = set()
for x, y in coordinates:
    newCo2.add((x, y))

listOfSets = [newCo2]

for i, fold in enumerate(folds):
    temp = []
    first, end = fold.split("=")
    if(first[-1] == "y"):
        for x, y in listOfSets[i]:
            if(y < int(end)):
                temp.append((int(end)-abs(x-int(end)), y))
            else:
                temp.append((x, y-int(end)))
    if(first[-1] == "x"):
        for x, y in listOfSets[i]:
            if(x > int(end)):
                temp.append((int(end)-abs(x-int(end)), abs(y-int(end))))
            else:
                temp.append((x, y))
    listOfSets.append(set(temp))

print(len(listOfSets)
# for i, set in enumerate(listOfSets):
#     print(folds[i])
#     print(set)
# x, y = zip(*set)
# plt.scatter(x, y)
# plt.show()

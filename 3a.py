from auth import getInput

input = getInput(3).text
list = input.split()

results = {}

final = {
    0: "",
    1: ""
}

for x in list:
    for i, y in enumerate(x):
        try:
            results[i] += int(y)
        except:
            results[i] = int(y)

for item in results.items():
    if(item[1] > len(list)/2):
        final[0] += "1"
        final[1] += "0"
    else:
        final[0] += "0"
        final[1] += "1"

print(int(final[0], 2)*int(final[1], 2))

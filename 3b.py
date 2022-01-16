from auth import getInput

input = getInput(3).text
ones = set()
zeros = set()


def getSetList(listList):
    list = set()
    for line in listList:
        list.add(line)
    return list


list = getSetList(input.split())

n = 0
k = 0
oxygen = True
rating = 0
rating2 = 0
while(len(list) > 1):
    for line in list:
        if(line[k] == "0"):
            zeros.add(line)
        if(line[k] == "1"):
            ones.add(line)
        n += 1
        if(n == len(list)):
            if(len(zeros) <= len(ones)):
                if(oxygen):
                    list = list - zeros
                else:
                    list = list - ones
                    print(list)
                zeros = set()
                ones = set()
                n = 0
                k += 1
                if(k == len(line)):
                    k = 0
            else:
                if(oxygen):
                    list = list - ones
                else:
                    list = list - zeros
                    print(list)
                ones = set()
                zeros = set()
                n = 0
                k += 1
                if(k == len(line)):
                    k = 0
    if(len(list) == 1 and oxygen):
        rating = list
        oxygen = False
        list = getSetList(input.split())
        n = 0
        k = 0

    if(len(list) == 1 and oxygen == False):
        rating2 = list

iterator = iter(rating)
num = int(next(iterator, None), 2)
iterator = iter(rating2)
print(int(next(iterator, None), 2) * num)

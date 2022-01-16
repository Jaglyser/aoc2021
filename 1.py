import re
import requests as rq
s = rq.Session()
r = rq.get('https://adventofcode.com/2021/day/1/input',
           cookies={'session': <COOKIE>})
list = []
index = 0
count = 0

for x in r.iter_lines():
    list.append(int(x.decode('ASCII')))

for num in list:
    try:
        sum1 = list[index] + list[index+1] + list[index+2]
        sum2 = list[index+1] + list[index+2] + list[index+3]
    except:
        print('error')
    if(sum2 > sum1):
        count = count + 1
    index = index + 1
print(count)

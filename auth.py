import requests as rq


def getInput(day: int):
    url = 'https://adventofcode.com/2021/day/%d/input' % (day)
    r = rq.get(url, cookies={
        'session': "53616c7465645f5fddc9931aac16cd503d2916d3685a3128b3bb047b133c1eb58a87aba37276060d96e236ee42c9ff17"})
    return r

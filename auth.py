import requests as rq


def getInput(day: int):
    url = 'https://adventofcode.com/2021/day/%d/input' % (day)
    r = rq.get(url, cookies={
        'session': <COOKIE>})
    return r

from auth import getInput
from math import ceil
from statistics import median
input = getInput(10).text

# input = "{([(<{}[<>[]}>{[]{[(<()>\n"+'[[<[([]))<([[{ }[[()]]]\n' + \
#     "[{[{({}]{}}([{[{{{}}([]\n"+"[<(<(<(<{}))><([]([]()\n" + \
#     "<{([([[(<>()){}]>(<<{{\n"

# input = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n(((({<>}<{<{<>}{[]{[]{}\n{<[[]]>}<{[{[{[]{()[[[]\n<{([{{}}[<[[[<>{}]]]>[]]\n"

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

brackets = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">"
}
onion = {
    "{": [],
    "[": [],
    "(": [],
    "<": []
}


def main(input):
    score = 0
    autoScore = []
    for line in input.splitlines():
        points2
        val = findError(line)
        try:
            score += findError(line)
        except:
            print("no syntax errors")
            autoScore.extend(val)
        onionPeeling()
    print(score)
    print(median(sorted(autoScore)))


def onionPeeling():
    for key, value in onion.items():
        onion[key] = []


def get_key(search):
    for open, close in brackets.items():
        if(close == search):
            return open


def find_bracket(value):
    for bracket, list in onion.items():
        if(value in list):
            onion[bracket].remove(value)
            return bracket


def findError(line):
    counter = 0
    for i, bracket in enumerate(line):
        if(bracket in brackets.keys()):
            counter += 1
            onion[bracket].append(counter)
        if(bracket in brackets.values()):
            open = get_key(bracket)
            layers = onion[open]
            if(len(layers) == 0):
                return points[bracket]
            if(layers[len(layers)-1] != counter):
                return points[bracket]
            counter -= 1
            onion[open] = layers[: -1]
    if(i == len(line) - 1):
        score2 = 0
        print("finding bracket order")
        for i in range(counter, 0, -1):
            brac = find_bracket(i)
            score2 = score2*5 + points2[brackets[brac]]
        return [score2]


if __name__ == "__main__":
    main(input)

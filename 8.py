from auth import getInput
from re import split
import itertools

input = getInput(8).text.splitlines()
counter = 0

for line in input:
    a, b = line.split(" | ")
    b = b.split(" ")
    for segment in b:
        if len(segment) in (2, 3, 4, 7):
            counter += 1
print(counter)

lex = {"acedgfb": 8, "cdfbe": 5, "gcdfa": 2, "fbcad": 3, "dab": 7,
       "cefabd": 9, "cdfgeb": 6, "eafb": 4, "cagedb": 0, "ab": 1}
lex = {"".join(sorted(k)): v for k, v in lex.items()}
ans = 0
for line in input:
    a, b = line.split(" | ")
    a = a.split(" ")
    b = b.split(" ")
    for perm in itertools.permutations("abcdefg"):
        pmap = {a: b for a, b in zip(perm, "abcdefg")}
        anew = ["".join(pmap[c] for c in x) for x in a]
        bnew = ["".join(pmap[c] for c in x) for x in b]
        if all("".join(sorted(an)) in lex for an in anew):
            bnew = ["".join(sorted(x)) for x in bnew]
            print(bnew)
            ans += int("".join(str(lex[x]) for x in bnew))
            break
print(ans)

from itertools import groupby

S = input()

result = [(len(list(g)), int(k)) for k, g in groupby(S)]

print(*result)
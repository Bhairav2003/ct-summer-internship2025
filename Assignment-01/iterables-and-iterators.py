from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())

allcombinations = list(combinations(range(N), K))

favorable = 0
for comb in allcombinations:
    if 'a' in [letters[i] for i in comb]:
        favorable += 1

probability = favorable / len(allcombinations)

print(f"{probability:.4f}")
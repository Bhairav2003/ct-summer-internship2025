# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())  
shoe_sizes = list(map(int, input().split()))
N = int(input())  

inventory = Counter(shoe_sizes)

earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1

print(earnings)
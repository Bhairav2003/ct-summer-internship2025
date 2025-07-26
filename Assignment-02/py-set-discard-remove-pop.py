# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())  
s = set(map(int, input().split()))  
N = int(input())  
for _ in range(N):
    parts = input().strip().split()
    cmd = parts[0]

    if cmd == "pop":
        if s: 
            s.pop()
    elif cmd == "remove":
        val = int(parts[1])
        if val in s:
            s.remove(val)
    elif cmd == "discard":
        s.discard(int(parts[1]))
print(sum(s))

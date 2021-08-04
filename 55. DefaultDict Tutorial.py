from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
B = []


for i in range(n):
    A[input()].append(i+1)

for _ in range(m):
    B.append(input())

for char in B:
    if char in A: 
        print(" ".join(map(str, A[char])))
    else:
        print(-1)
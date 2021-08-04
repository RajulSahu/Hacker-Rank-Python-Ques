from itertools import product

N, M = map(int, input().split())

li = []
for _ in range(N):
    arr = list(map(int, input().split()))[1:]
    li.append(arr)

output = map(lambda x: sum(i * i for i in x) % M, product(*li))
print(max(output))
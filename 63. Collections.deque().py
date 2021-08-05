from collections import deque

N = int(input())
d = deque()

for _ in range(N):
    inp = input().split()
    operation = inp[0]
    args = tuple(map(int, inp[1:]))
    eval(f"d.{operation}{args}")

print(*d)
import re

N = int(input())
for _ in range(N):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)
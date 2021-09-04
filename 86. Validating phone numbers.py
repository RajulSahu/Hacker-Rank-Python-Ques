import re
n = int(input())

pattern = re.compile("[7-9][0-9]{9}$")

for _ in range(n):
    ph = input()
    if pattern.match(ph):
        print("YES")
    else:
        print("NO")


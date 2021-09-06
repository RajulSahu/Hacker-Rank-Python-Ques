import re
n = int(input())
pattern = re.compile("<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>")

for _ in range(n):
    name, s = input().split(" ")
    match = re.match(pattern, s)
    if match:
        print(name, s)
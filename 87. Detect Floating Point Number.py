import re

n = int(input())
pattern = re.compile("^[-+]?[0-9]*\.[0-9]+$")

for _ in range(n):
    d = input()
    if pattern.match(d):
        print(True)
    else:   
        print(False)
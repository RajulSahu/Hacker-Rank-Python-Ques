import re


s = input()
k = input()
pattern = re.compile(k)
searched = pattern.search(s)
if not searched:
    print((-1, -1))
while searched:
    print((searched.start(), searched.end()-1))
    searched = pattern.search(s, searched.start()+1)


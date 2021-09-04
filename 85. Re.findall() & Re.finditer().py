import re

s = input()
c = "bcdfghjklmnpqrstvwxyz"
v = "aeiou"
l = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), s, flags=re.IGNORECASE)

if not l:
    print(-1)
else:
    print("\n".join(l))
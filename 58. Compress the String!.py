from itertools import groupby

S = input()
for k , c in groupby(S):
    print( (len(list(c)), int(k)), end = " ")


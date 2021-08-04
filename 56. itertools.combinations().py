from itertools import combinations, permutations

inp = input().split()
string = inp[0]
word_count = int(inp[1])

string = sorted(string)

for i in range(1, word_count+1):
    outputs = list(combinations(string, i))
    for output in outputs:
        print("".join(output))




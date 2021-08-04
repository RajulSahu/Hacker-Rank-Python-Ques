from itertools import combinations_with_replacement


inp = input().split()
string = inp[0]
word_count = int(inp[1])

string = sorted(string)

outputs = list(combinations_with_replacement(string, word_count))

for output in outputs:
    print("".join(output))




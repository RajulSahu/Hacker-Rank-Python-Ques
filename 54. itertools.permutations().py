from itertools import permutations

inp = input().split()
string = inp[0]
word_length = int(inp[1])

string_lst = []
string_lst[:0] = string
string_lst.sort()
string = string_lst


all_permutations = list(permutations(string, word_length))
for item in all_permutations:
    print("".join(item))

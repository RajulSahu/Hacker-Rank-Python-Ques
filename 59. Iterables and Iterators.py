from itertools import combinations, permutations

N = int(input())
S = input().split()
k = int(input())


all_combinations = list(combinations(S, k))
filtered_result = list(filter(lambda c: 'a' in c, all_combinations))

print("{0:.3f}".format(len(filtered_result)/len(all_combinations)))



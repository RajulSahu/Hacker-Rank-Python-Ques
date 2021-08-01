n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
symm_diff = list(a.symmetric_difference(b))
symm_diff.sort()
for value in symm_diff:
    print(value)
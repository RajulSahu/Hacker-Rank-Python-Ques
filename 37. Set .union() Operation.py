n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

union_set = a.union(b)
print(len(union_set))
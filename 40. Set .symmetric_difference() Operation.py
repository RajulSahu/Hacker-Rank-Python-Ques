n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

symmetric_difference_set = a.symmetric_difference(b)
print(len(symmetric_difference_set))



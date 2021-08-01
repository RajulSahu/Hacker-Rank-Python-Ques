n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

difference_set = a.difference(b)
print(len(difference_set))



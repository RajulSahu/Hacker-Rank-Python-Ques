n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

intersection_set = a.intersection(b)
print(len(intersection_set))

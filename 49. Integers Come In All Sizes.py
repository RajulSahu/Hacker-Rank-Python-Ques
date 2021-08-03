a = int(input())
b = int(input())
c = int(input())
d = int(input())

if all([1 <= a <= 1000, 1 <= b <= 1000, 1 <= c <= 1000, 1 <= d <= 1000]):
    print(pow(a,b) + pow(c,d))
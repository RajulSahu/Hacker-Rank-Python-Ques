def no_idea(arr, A, B):
    happiness = 0
    for value in arr:
        if value in A:
            happiness += 1
        elif value in B:
            happiness -= 1
        
    print(happiness)


n_m = input()
n = int(n_m.split()[0])
m = int(n_m.split()[1])

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
if 1 <= n <= 10**5 and 1 <= m <= 10**5:
    no_idea(arr, A, B)
def check_subset(A, B):
    print(A.issubset(B))




nos_test_case = int(input())

for _ in range(nos_test_case):
    n_A = int(input())
    A = set(map(int, input().split()))
    n_B = int(input())
    B = set(map(int, input().split()))
    check_subset(A, B)
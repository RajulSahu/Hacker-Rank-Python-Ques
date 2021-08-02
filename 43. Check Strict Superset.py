def Check_strict_superset(A , B):
    if A  > B:
        return True
    else:
        return False
    


A = set(map(int, input().split()))

num_of_subsets = int(input())
result = []
for _ in range(num_of_subsets):
    B = set(map(int, input().split()))
    ans = Check_strict_superset(A , B)
    result.append(ans)
print(all(result))

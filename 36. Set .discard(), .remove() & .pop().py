n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    operation_str = input()
    function = operation_str.split()[0]
    args = tuple(map(int, operation_str.split()[1:]))
    if len(args) == 0:
        eval(f"s.{function}")
    eval(f"s.{function}{args}")
print(sum(list(s)))

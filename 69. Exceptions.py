def perform_operation(a, b):
    try:
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code:", e)


N = int(input())
for i in range(N):
    inp = input().split()
    perform_operation(inp[0], inp[1])



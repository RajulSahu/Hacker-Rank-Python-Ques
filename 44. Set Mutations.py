def perform_operation(A, B, instruction):
    eval(f"A.{instruction}(B)")
    
    
    

N = int(input())
A = set(map(int, input().split()))

k = int(input())
for _ in range(k):
    instruction = input().split()[0]
    B = set(map(int, input().split()))
    perform_operation(A, B, instruction)
print(sum(A))
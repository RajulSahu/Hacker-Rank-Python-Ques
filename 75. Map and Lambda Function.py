cube = lambda x: pow(x,3) 

def fibonacci(n):
    a = -1
    b = 1
    fib = []
    for i in range(n):
        c = a+b
        a = b
        b = c
        fib.append(c)
    return fib
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
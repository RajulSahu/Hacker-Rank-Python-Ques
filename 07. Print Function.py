def print_it(n):
    for i in range(1, n+1):
        print(str(i), end="")

if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:
        print_it(n)
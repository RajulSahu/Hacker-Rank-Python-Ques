def task(n):
    if 1 <= n <= 20:
        for i in range(n):
            print(i*i)

if __name__ == '__main__':
    n = int(input())
    task(n)

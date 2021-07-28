def print_formatted(number):
    max_len = len("{0:b}".format(number))
    if 1 <= number <= 99:
        for num in range(1, number+1):
            print("{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(num, w=max_len))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
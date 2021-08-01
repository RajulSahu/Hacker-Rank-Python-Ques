n = int(input())
if 0 <= n <= 1000:
    countries = []
    for i in range(n):
        countries.append(input())

    countries = set(countries)
    print(len(countries))
def calculate(a, b):
    int_division = a//b
    float_division = a/b
    print(int_division)
    print(float_division)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    calculate(a, b)
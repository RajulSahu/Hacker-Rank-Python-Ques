import numpy
numpy.set_printoptions(legacy='1.13')


a, b = map(int, input().strip().split(" "))

if a == b:
    print(numpy.identity(a))
else:
    print(numpy.eye(a, b))


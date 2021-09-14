import numpy

A = numpy.array(input().strip().split(), float)
x = int(input())

print(numpy.polyval(A, x))
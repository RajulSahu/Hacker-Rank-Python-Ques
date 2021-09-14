import numpy


n = int(input())

A = numpy.array([input().strip().split() for _ in range(n)], float)

det = numpy.linalg.det(A)

print(round(det, 2))


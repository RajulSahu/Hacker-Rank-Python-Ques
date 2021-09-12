import numpy

n, m, p = map(int, input().strip().split(" "))

array1 = numpy.array([input().strip().split(" ") for _ in range(n)], int)
array2 = numpy.array([input().strip().split(" ") for _ in range(m)], int)

array3 = numpy.concatenate((array1, array2))
print(array3)



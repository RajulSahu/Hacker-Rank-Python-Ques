import numpy


n, m = map(int, input().strip().split(" "))

a = numpy.array([input().strip().split(" ") for _ in range(n)], int)

sum_arr = numpy.sum(a, axis=0)
product = numpy.prod(sum_arr, axis = None)

print(product)
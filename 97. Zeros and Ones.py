import numpy

dimension = tuple(map(int, input().strip().split()))

zero_array = numpy.zeros(dimension, dtype = int)

one_array = numpy.ones(dimension, dtype = int)


print(zero_array)
print(one_array)


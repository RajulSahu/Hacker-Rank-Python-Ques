import numpy

n , m = map(int, input().strip().split(" "))

my_array = numpy.array([input().strip().split(" ") for _ in range(n)], int)


print(numpy.max(numpy.min(my_array, axis = 1), axis = None))

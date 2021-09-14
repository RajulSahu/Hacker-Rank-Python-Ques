import numpy

n, m = map(int, input().strip().split())

my_array = numpy.array([input().strip().split() for _ in range(n)], int)



mean = numpy.mean(my_array, axis = 1)
var = numpy.var(my_array, axis = 0)
std = numpy.std(my_array, axis = None)
std_formatted = "{0:.11f}".format(std) if std > 0 else 0.0

print(mean)
print(var)
print(std_formatted)



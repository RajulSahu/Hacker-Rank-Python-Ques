import numpy

arr = list(map(int, input().strip().split(" ")))
nump_arr = numpy.array(arr)
nump_arr.shape = (3, 3)
print(nump_arr)






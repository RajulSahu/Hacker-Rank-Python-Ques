import numpy

def arrays(arr):
    nums = numpy.array(arr, float)
    return numpy.flip(nums)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
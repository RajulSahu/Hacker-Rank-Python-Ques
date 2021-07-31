def average(array):
    arr_set = list(set(array))
    average = "{:.3f}".format(sum(arr_set)/len(arr_set))
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
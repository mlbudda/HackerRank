# Mini-Max Sum

# arr = list(map(int, input().rstrip().split()))

def miniMaxSum(arr):
    """ Finds the minimum and maximum values that can be 
    calculated by summing exactly four of the five integers """
    sum_min = 0
    sum_max = 0
    for i in range(4):
        sum_min += sorted(arr)[i]
        sum_max += sorted(arr, reverse=True)[i]
    return print(sum_min, sum_max)


miniMaxSum([1,2,3,4,5]) # 10 14



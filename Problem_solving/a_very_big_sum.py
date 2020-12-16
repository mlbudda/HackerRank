# A Very Big Sum

# ar_count = int(input())
# ar = list(map(int, input().rstrip().split()))


def aVeryBigSum(ar):
    """ Returns the integer sum of the elements in the array """
    sum = 0
    for i in ar:
        sum += i
    return sum

# Running some tests..
print(aVeryBigSum([
    1000000001, 1000000002,1000000003,
    1000000004,1000000005]) == 5000000015)
# %%
# Simple Array Sum

# default input:
# ar_count = int(input())
# ar = list(map(int, input().rstrip().split()))

def simpleArraySum(ar):
    """ Finds the sum of its elements """
    sum = 0
    for i in ar:
        sum += i
    return sum

# Running some tests..
print(simpleArraySum([1, 2, 3, 4, 10, 11]) == 31)

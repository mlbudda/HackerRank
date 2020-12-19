# Plus Minus

# arr = list(map(int, input().rstrip().split()))

def plusMinus(arr):
    """ Calculates the ratios of its elements 
    that are positive, negative, and zero """
    pos = 0
    neg = 0
    zeros = 0
    for i in arr:
        if i > 0:
            pos +=1
        elif i < 0:
            neg +=1
        else:
            zeros +=1
    result = f'{pos/len(arr):.6f}\n{neg/len(arr):.6f}\n{zeros/len(arr):.6f}'
    return print(result)


# Running some tests...
plusMinus([-4, 3, -9, 0, 4, 1]) #  0.500000,0.333333,0.166667
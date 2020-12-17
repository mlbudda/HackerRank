# Diagonal Difference

# n = int(input().strip())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))

def diagonalDifference(arr):
    """ Calculates the absolute difference between 
    the sums of its diagonals """
    
    sum1 = 0
    sum2 = 0
    counter = 0
    for i in arr:
        sum1 += i[counter]
        sum2 += i[-(counter+1)]
        counter += 1
    return abs(sum1 - sum2)


# Running some tests..
print(diagonalDifference([
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]) == 15)
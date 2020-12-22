# Birthday Cake Candles

# candles_count = int(input().strip())
# candles = list(map(int, input().rstrip().split())) 

def birthdayCakeCandles(candles):
    """ Counts how many candles are tallest """
    return candles.count(sorted(candles, reverse=True)[0])


# Runnign some tests
print(birthdayCakeCandles([3,2,1,3]) == 2)
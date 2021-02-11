#%%
from numpy import average

# Vanilla Python, no library
def weightedMeanFunc1(numbers,weights):
    result_numbers = 0
    result_weights = 0
    for i in range(len(numbers)):
        result_numbers += numbers[i] * weights[i]
        result_weights += weights[i]
    return round(result_numbers/result_weights, 1)

print(weightedMeanFunc1([10, 40, 30, 50, 20], [1, 2, 3, 4, 5]) == 32.0)

#%%
# Using numpy average
def weightedMeanFunc2(numbers, weights):
    return round(average(numbers, weights=weights),1)

print(weightedMeanFunc2([10, 40, 30, 50, 20], [1, 2, 3, 4, 5]) == 32.0)
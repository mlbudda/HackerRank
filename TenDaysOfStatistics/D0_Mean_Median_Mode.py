#%%
import numpy as np
from scipy import stats

def meanMedianMode(numbers):
    numberMean = np.mean(numbers)
    numberMedian = np.median(numbers)
    numberMode = stats.mode(numbers)[0][0]
    return f'{numberMean}\n{numberMedian}\n{numberMode}'

print(meanMedianMode([64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]))
# 43900.6
# 44627.5
# 4978

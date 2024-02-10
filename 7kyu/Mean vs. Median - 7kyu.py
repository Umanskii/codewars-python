"""
Your goal is to implement the method meanVsMedian which accepts an odd-length array of integers and returns one of the following:

'mean' - in case mean value is larger than median value
'median' - in case median value is larger than mean value
'same' - in case both mean and median share the same value
Reminder: Median

Array will always be valid (odd-length >= 3)
"""
from numpy import mean, median

def mean_vs_median(numbers):
    if mean(numbers) > median(numbers):
        return 'mean'
    elif mean(numbers) < median(numbers):
        return 'median'
    else:
        return 'same'
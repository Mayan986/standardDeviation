import math

def standardDeviation(numbers):
    summation = sum(numbers)
    sample = len(numbers)
    mean = (summation / sample)
    print("Mean :", mean)
    l = []
    for i in numbers:
        l.append(math.pow(abs(i - mean), 2))
    sdsum = sum(l)
    root = math.sqrt(sdsum / (sample - 1))
    return root

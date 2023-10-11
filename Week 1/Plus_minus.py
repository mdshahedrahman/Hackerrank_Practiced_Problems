#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    count_zero = 0
    count_positive = 0
    count_negative = 0

    for i in arr:
        if i > 0:
            count_positive += 1
        elif i < 0:
            count_negative += 1
        else:
            count_zero += 1

    zero = count_zero / len(arr)
    positive = count_positive / len(arr)
    negative = count_negative / len(arr)

    frac_zero = f"{zero:.6f}"
    frac_positive = f"{positive:.6f}"
    frac_negative = f"{negative:.6f}"

    print(frac_positive)
    print(frac_negative)
    print(frac_zero)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

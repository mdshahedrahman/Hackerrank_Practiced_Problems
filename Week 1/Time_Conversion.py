import math
import os
import random
import re
import sys
from datetime import datetime


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    # Parse the input time string in 12-hour format
    time_12_hour_obj = datetime.strptime(s, "%I:%M:%S%p")

    # Format the time in 24-hour format
    time_24_hour = time_12_hour_obj.strftime("%H:%M:%S")

    return time_24_hour


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

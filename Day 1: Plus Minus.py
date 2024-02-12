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
    
    zero_arr, positive_arr, negative_arr = 0, 0, 0
    
    for i in range(0, len(arr)):
        if arr[i] == 0:
            zero_arr += 1
        elif arr[i] < 0:
            negative_arr += 1
        elif arr[i] > 0:
            positive_arr += 1
                
    
    print("{:.6f}".format(positive_arr/len(arr)))
    print("{:.6f}".format(negative_arr/len(arr)))
    print("{:.6f}".format(zero_arr/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

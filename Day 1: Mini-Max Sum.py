#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    first_val = 0
    second_val = 0
    arr.sort()
    
    for i in range(0, len(arr)-1):
        first_val += arr[i]
    for i in range(1, len(arr)):
        second_val += arr[i]
    
    print(first_val, second_val)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

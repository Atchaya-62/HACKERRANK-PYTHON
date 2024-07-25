#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    li = s.split(" ")
        
    s = li[0].capitalize()
    for i in range(1, len(li)):
        s += " " + li[i].capitalize()
    
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

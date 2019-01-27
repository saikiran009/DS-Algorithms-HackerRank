#!/bin/python
'''
We define a magic square to be an n*n  matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
'''

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.


all_magic_matrices = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
all_costs = []
def formingMagicSquare(s):
    for m in all_magic_matrices:
        cost = 0
        for j in xrange(3):
            for k,l in zip(m[j],s[j]):
                cost = cost + abs(k-l)
        all_costs.append(cost)
    return min(all_costs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

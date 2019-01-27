'''Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k'''

#!/bin/python

import math
import os
import random
import re
import sys
#from collections import defaultdict
# Complete the nonDivisibleSubset function below.


def nonDivisibleSubset(k, S):
    list_ = [0]*k
    for m in S:
        list_[m%k] = list_[m%k] +1
    sum_ = min(list_[0],1)

    for j in range(1,(k)/2 +1):
        if j != k-j:
            sum_ = sum_ + max(list_[j],list_[k-j])
        else:
            sum_ = sum_ + min(list_[j],1)
    return sum_



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = map(int, raw_input().rstrip().split())

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()

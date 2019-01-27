'''
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
For example, given the word w=abcd, the next largest word is abdc.

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.

biggerIsGreater has the following parameter(s):

w: a string
Input Format

The first line of input contains T, the number of test cases. 
Each of the next T lines contains w.
'''

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    sort_ = list(w)
    m = 1
    index = -1
    while m < len(w):
        if w[-m] > w[-m - 1]:
            index = m + 1
            break
        else:
            m = m + 1
    if index > -1:
        #value = len(w) - index
        n = 1

        while n <= index:
            if sort_[-n] > sort_[-index]:
                
                temp = sort_[-n]
                
                sort_[-n] = sort_[-index]
                sort_[-index] = temp
                break
            else:
                n = n + 1
        w = ''.join(sort_)
        # flip a string from index position to end
        if index >2:
            substring = w[-index+1:][::-1]
            complete_string = w[:-index+1] + substring
        else:
            complete_string = w
    else:
        complete_string = 'no answer'
    return complete_string




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(raw_input())

    for T_itr in xrange(T):
        w = raw_input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()



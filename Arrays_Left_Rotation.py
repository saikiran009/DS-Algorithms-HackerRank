'''

A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of integers) and  (the number of left rotations you must perform). 
The second line contains  space-separated integers describing the respective elements of the array's initial state.

for more details: https://www.hackerrank.com/challenges/ctci-array-left-rotation
'''

count = 0
def array_left_rotation(a, n, k):
   shift_1 = abs(n-k)
   b = a[:] #So that when u perform changes on b list a list is not effected
   for m in xrange(n):
       if ((n-1)-(m)) >= shift_1:
           b[m +shift_1] = a[m]
       else:
           b[(shift_1-((n-1)-(m))-1)] = a[m]
   return b
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

'''
You have the prices of n dresses arranged in a line. You have to select any number of dresses such as to get the max sum of prices. But, You cannot choose adjacent dresses.

Input Format

First line contains an integer n. The next line contains n integers which denote the prices of the n dresses.

Example: 4 3 4 5 10

Constraints: n <= 100000 each of the prices < 10e9

Output Format

One integer which is the max price you could obtain by choosing the set of dresses optimally.

Sample Input

4
3 4 5 10
Sample Output

14

Explanation

select 4 and 10


For more details: https://www.hackerrank.com/contests/bits-goa-day-3/challenges/spendthrift-shopper/problem
'''


length = int(raw_input())
price = map(int,raw_input().split())
sum_max = [0]*length

def max_sum():
    for m in xrange(len(price)):
        if m == 0 or m ==1:
           sum_max[m] = price[m]
        else:
            sum_max[m] = max(sum_max[m-1] , sum_max[m-2]+price[m])

    return sum_max.pop()

print max_sum()
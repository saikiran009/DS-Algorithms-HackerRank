'''You'll be given a number n, which would be followed by n lines of numbers A1, A2, .... , An.

If

Ai == 0 : You have to print the maximum amongst all the numbers seen till now.
Ai == -1 : Delete the last element. (i.e this element wouldn't be considered from now on)
Note that 0, -1, wouldn't be added to the pool of numbers which you are using to find the maximum or deletion.

Constraints

n <= 10^6
Ai <= 10^9
Input Format

First line would contain n, n lines would follow consisting of A1, A2 ... An. (One in each line)

Output Format

For each 0 encountered print the maximum element from the pool. (Ignoring 0 and -1 that you have seen).

For each -1 encountered delete the last element from the pool.

Note that the answer to each 0 and -1 queries should be printed in a new line.

Sample Input

10  
5
0
-1
10
7
0
12
0
-1
0
Sample Output

5
10
12
10
'''




number_of_integers = int(raw_input())

list_of_numbers = []
for number in xrange(number_of_integers):
    current_number = int(raw_input())
    if current_number > 0:
        max_number = current_number
        if list_of_numbers and current_number < list_of_numbers[-1]:
            max_number = list_of_numbers[-1]
        list_of_numbers.append(max_number)
    elif current_number == 0:
        print list_of_numbers[-1]
    elif current_number == -1:
        list_of_numbers.pop()

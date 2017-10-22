'''Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.


Input Format

The first line contains a single string, a. 
The second line contains a single string, b.

Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc
Sample Output

4

For more details : https://www.hackerrank.com/challenges/ctci-making-anagrams/submissions

'''

from collections import Counter

def number_needed(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)
    b_dict.subtract(a_dict)
    answer = sum(abs(i) for i in b_dict.values())
    return answer
    
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
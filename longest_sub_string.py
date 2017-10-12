

''''Sample input
5 6
1 2 3 4 1
3 4 1 2 1 3
'''

'''Sample output
1 2 3
'''
''' For further details https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem'''
'''Format of the input'''
lengths = raw_input().split(' ')
length_str_1 = int(lengths[0])
length_str_2 = int(lengths[1])
string1 = map(int,raw_input().split(' '))
string2 = map(int,raw_input().split(' '))
matched_string = []
output_string = []

'''Get the longest common substring'''

def lcs_list(index_i,index_j,value):
    while index_i and index_j > 0:
        if value == max(matched_string[index_i][index_j-1],matched_string[index_i-1][index_j]):
            if matched_string[index_i][index_j-1] > matched_string[index_i-1][index_j]:
                index_i = index_i
                index_j = index_j -1
            else:
                index_j = index_j
                index_i = index_i-1
            value = value

        elif value > max(matched_string[index_i][index_j-1],matched_string[index_i-1][index_j]):
            output_string.append(string2[index_j-1])
            index_i = index_i -1
            index_j = index_j -1
            value = matched_string[index_i][index_j]
        else:
            pass




'''Find the lenght of of the lcs by building the matrix'''

def lcs_1(string1,string2):
    for i in xrange(length_str_1+1):
        matched_string.append([0] * (length_str_2+1))

    for i in xrange(length_str_1+1):
        for j in xrange(length_str_2+1):
            if i ==0 or j ==0:
                matched_string[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                matched_string[i][j] = matched_string[i-1][j-1] +1
            else:
                matched_string[i][j] = max(matched_string[i][j-1],matched_string[i-1][j])
    value = matched_string[length_str_1][length_str_2]
    lcs_list(length_str_1,length_str_2,value)
    return value

value = lcs_1(string1,string2)
output_string.reverse()
output_string = map(str,output_string)
print ' '.join(output_string)



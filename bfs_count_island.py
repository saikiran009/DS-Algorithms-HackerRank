list_of_size = raw_input().split(' ')
no_of_rows = int(list_of_size[0])
no_of_columns = int(list_of_size[1])
matrix =[]


for m in xrange(no_of_rows):
    matrix.append(map(int,raw_input().rstrip().split(' ')))
big_visited = []
'''Initalising the visited matrix whether the node is visited or not'''
for i in xrange(no_of_rows):
    visited = []
    for j in xrange(no_of_columns):
        visited.append(0)
    big_visited.append(visited)

'''Taking the neighbouring cells'''
neighbours = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,-1],[1,1],[-1,1]]
def get_neighbours(a,b):
    for j in neighbours:
        if a + j[0] < no_of_rows and b +j[1] < no_of_columns and a+j[0] > -1 and b + j[1] > -1 and matrix[a+j[0]][b+j[1]] == 1 and big_visited[a+j[0]][b+j[1]] == 0 :
            big_visited[a +j[0]][b+j[1]] = 1
            get_neighbours(a+j[0],b+j[1])
        else:
           
            pass

'''Visit nodes which are not visited before and having value 1 and find their neighbours'''
def count_1():
    count = 0
    for i in xrange(no_of_rows):
        for j in xrange(no_of_columns):
            if matrix[i][j] == 1 and big_visited[i][j] == 0:
                big_visited[i][j] = 1
                get_neighbours(i,j)
                #print matrix[i][j]
                count = count + 1
            else:
                pass
                
    return count
print count_1()






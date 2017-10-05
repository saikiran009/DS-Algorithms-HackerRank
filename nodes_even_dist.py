'''Problem Statement


You are given a tree (a simple connected graph with no cycles). The tree has N nodes numbered from 1 to N and is rooted at node 1.

Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes.

Input Format

The first line of input contains two integers N and M. N is the number of nodes, and M is the number of edges. 
The next M lines contain two integers ui and  vi which specifies an edge of the tree.



Note: The tree in the input will be such that it can always be decomposed into components containing an even number of nodes.

Output Format

Print the number of removed edges.

Sample Input

10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
Sample Output

2

'''





''' Get the input in the desired matrix format'''



nodes_edges = raw_input().split(' ')
nodes = int(nodes_edges[0])
edges = int(nodes_edges[1])
graph_matrix = []
edges_list = []

'''Create Graph matrix'''
for m in xrange(nodes):
    graph_matrix.append([0 for m in xrange(nodes)])


'''Edge list'''
for k in xrange(edges):
    edge = [int(m) for m in  raw_input().split(' ')]
    edges_list.append(edge)
    graph_matrix[edge[0]-1][edge[1]-1] = 1
    graph_matrix[edge[1]-1][edge[0]-1] = 1



'''DfS to search for the number of children for that node'''
def dfs(m,visited_nodes):
    count = 1
    for k in xrange(nodes):
        if visited_nodes[k] == 0 and graph_matrix[m][k] == 1:
            visited_nodes[k] =1
            count = count + dfs(k,visited_nodes)
        else:
            pass
    return count

'''Iterate over each edge to see whether it can be broken or not'''
edge_remove =0
def go_edge():
    global edge_remove
    for ed in edges_list:
        visited_nodes = [0] * nodes
        visited_nodes[ed[0]-1] = 1
        visited_nodes[ed[1]-1] =1
        count_1 = dfs(ed[0]-1,visited_nodes)
        count_2 = dfs(ed[1]-1,visited_nodes)
        if count_1 > 0 and count_2 > 0 and (count_1) %2 ==0 and (count_2) %2 == 0:
            edge_remove = edge_remove + 1
            graph_matrix[ed[0]-1][ed[1]-1] = 0
            graph_matrix[ed[0]-1][ed[1]-1] =0
        else:
            pass
    return edge_remove
print go_edge()

'''For more details about the problem visit this link https://www.hackerrank.com/challenges/even-tree/problem'''
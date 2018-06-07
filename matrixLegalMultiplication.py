#!/usr/bin/python3

'''            Legal Longest Matrix Multiplication Order - Using BFS
                         Complexity is O(N^4)
'''

from collections import defaultdict

ma=[-1,0,[]]

def breadthFirstSearch(d, V, mat,s,dist):
    global ma
    for i in range(1,V+1):
        mat[i][0]='white'
        mat[i][2]=[]
    q = [s]
    mat[s][0]='gray'
    while q:
        u = q.pop(0)
        mat[u][0]='black'
        if d.get(u):
            for v in d[u]:
                if mat[v][0]=='white':
                    q.append(v)
                    mat[v][0] ='gray'
                    mat[v][2]=[u]
                    mat[v][2].extend(mat[u][2])
                    dist[s][v]=dist[s][u]+1
                    if dist[s][v]>ma[0]:
                        ma[0]=dist[s][v]
                        ma[1]=v
                        ma[2]=mat[v][2]

                elif mat[v][0]=='black':
                    if v not in mat[u][2]:
                        if dist[s][u]+1>dist[s][v]:
                            q.append(v)
                            mat[v][0] = 'gray'
                            mat[v][2] = [u]
                            mat[v][2].extend(mat[u][2])
                            dist[s][v] = dist[s][u] + 1
                            if dist[s][v] > ma[0]:
                                ma[0] = dist[s][v]
                                ma[1] = v
                                ma[2] = mat[v][2]
                else:
                    if v not in mat[u][2]:
                        if dist[s][u]+1>dist[s][v]:
                            mat[v][2] = [u]
                            mat[v][2].extend(mat[u][2])
                            dist[s][v] = dist[s][u] + 1
                            if dist[s][v] > ma[0]:
                                ma[0] = dist[s][v]
                                ma[1] = v
                                ma[2] = mat[v][2]


V = int(input('Enter the number of Matrices : '))
mat = [0]
print('Enter the dimensions of matrix each on new line with space like :')
print('1 2\n2 3\n3 4\n')
for i in range(V):
    n,m=map(int,input().split())
    mat.append(['white',(n,m),[]])
d = defaultdict(list)
for i in range(1,V+1):
    for j in range(i+1,V+1):
        if mat[i][1][1] == mat[j][1][0]:
            d[i].append(j)
        if mat[i][1][0] ==mat[j][1][1]:
            d[j].append(i)

dist = [[0]*(V+1) for i in range(V+1)]

for i in range(1,V+1):
    breadthFirstSearch(d,V,mat,i,dist)

print('Order is : ')
for i in reversed(ma[2]):
    print(mat[i][1],end=" ")
print(mat[ma[1]][1])

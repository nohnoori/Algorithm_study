from collections import deque

t=int(input())

vec=[(1,0),(-1,0),(0,-1),(0,1)]

def bfs(graph,root):
    queue=deque([root])
    while queue:
        x,y=queue.popleft()
        graph[x][y]=0
        for v in vec:
            if x+v[0] < 0 or x+v[0] >=n or y+v[1] < 0 or y+v[1] >= m:
                continue
            if graph[x+v[0]][y+v[1]] == 1:
                graph[x+v[0]][y+v[1]]=0
                queue.append((x+v[0], y+v[1]))
    return graph

for _ in range(t):
    count=0
    n,m,k=map(int,input().split(' '))
    graph=[[0]*m for _ in range(n)]
    
    for _ in range(k):
        x,y=map(int,input().split(' '))
        graph[x][y]=1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                count+=1
                graph=bfs(graph,(i,j))
    print(count)

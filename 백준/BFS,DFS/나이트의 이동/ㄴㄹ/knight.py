from collections import deque
T=int(input())
vec=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

for i in range(T):
    n=int(input())
    start=list(map(int,input().split()))
    end=list(map(int,input().split()))
    visited=[[-1]*n for _ in range(n)]
    queue=deque([start])
    while queue:
        x,y=queue.popleft()
        if x==end[0] and y==end[1]:
            print(visited[x][y]+1,end='\n')
            break
        for v in vec:
            if 0<=x+v[0]<n and 0<=y+v[1]<n:
                if visited[x+v[0]][y+v[1]]==-1:
                    queue.append((x+v[0],y+v[1]))
                    visited[x+v[0]][y+v[1]]=visited[x][y]+1

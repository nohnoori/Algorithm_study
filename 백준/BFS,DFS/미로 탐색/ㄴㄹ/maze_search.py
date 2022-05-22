from sys import stdin
n,m = map(int, stdin.readline().split())
graph=[stdin.readline().rstrip() for _ in range(n)]
vec=[(1,0),(-1,0),(0,1),(0,-1)]
dis=[[0]*m for _ in range(n)]
dis[0][0]=1

queue=[(0,0)]

while queue:
    x,y=queue.pop(0)
    if x==n-1 and y==m-1:
        print(dis[x][y])
        break
    for v in vec:
        nx=x+v[0]
        ny=y+v[1]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='1' and dis[nx][ny]==0:
            dis[nx][ny]=dis[x][y]+1
            queue.append((nx,ny))

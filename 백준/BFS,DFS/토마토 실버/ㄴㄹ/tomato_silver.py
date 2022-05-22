from collections import deque

m,n=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(n)]
vec=[[1,0],[-1,0],[0,-1],[0,1]]
que=deque([])
ans=0

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            que.append([i,j])
def bfs():
    while que:
        x,y=que.popleft()
        for v in vec:
            dx,dy=x+v[0],y+v[1]
            if 0<=dx<n and 0<=dy<m and box[dx][dy]==0:
                box[dx][dy]=box[x][y]+1
                que.append([dx,dy])
bfs()
for i in range(n):
    for j in range(m):
        if box[i][j]==0:
            print(-1)
            exit(0)
    ans=max(ans,max(box[i]))
print(ans-1)

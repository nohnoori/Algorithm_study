import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
box = []
queue = deque([])
ans=0

for k in range(h):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int,input().split())))
        for j in range(m):
            if tmp[i][j]==1:
                queue.append([i,j,k])
    box.append(tmp)
    
vec=[[1,0,0],[-1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1]]

def bfs():
    while queue:
        x,y,z=queue.popleft()
        for v in vec:
            dx,dy,dz=x+v[0],y+v[1],z+v[2]
            if 0<=dx<n and 0<=dy<m and 0<=dz<h and box[dz][dx][dy]==0:
                box[dz][dx][dy]=box[z][x][y]+1
                queue.append([dx,dy,dz])
                
bfs()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j]==0:
                print(-1)
                exit(0)
        ans=max(ans,max(box[k][i]))
print(ans-1)

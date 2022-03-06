from collections import deque

def func(seat,r,c):
    queue=deque([(r,c,0)])
    visited=[]
    vec=[[0,1],[1,0],[0,-1],[-1,0]]

    while queue:
        r,c,d=queue.popleft()
        visited.append((r,c))
        for v in vec:
            xr=r+v[0]
            yc=c+v[1]
            dis=d+1
            if 0<=xr<5 and 0<=yc<5 and (xr,yc) not in visited:
                visited.append((xr,yc))
                if seat[xr][yc]=='P':
                    if dis<3:
                        return 0
                elif seat[xr][yc]=='O':
                    if dis==1:
												#처음 P 발견한 구간에서 dis 거리만큼 떨어져 있음
												#dis만큼 떨어진 곳에서 다시 bfs 탐색
                        queue.append((xr,yc,dis))
    return 1

def solution(places):
    answer = []

    for place in places:
        ans=1
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    result=func(place,i,j)
                    if result==0:
                        ans=0
        answer.append(ans)

    return answer

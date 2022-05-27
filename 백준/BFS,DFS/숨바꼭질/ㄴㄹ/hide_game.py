from collections import deque
n,m=map(int,input().split())
queue=deque([n])
visited=[0]*100001

while queue:
    loc=queue.popleft()
    if loc==m:
        print(visited[loc])
        break
    for v in [loc+1,loc-1,loc*2]:
        if 0<=v<=100000 and not visited[v]:
            visited[v]=visited[loc]+1
            queue.append(v)

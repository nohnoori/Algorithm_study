from collections import deque
n=list(map(int,input().split(' ')))
diction={}

for i in range(n[1]):
    a,b=map(int,input().split(' '))
    if a not in diction:
        diction[a]=[b]
    elif b not in diction[a]:
        diction[a].append(b)
    diction[a].sort()
    
    if b not in diction:
        diction[b]=[a]
    elif a not in diction[b]:
        diction[b].append(a)
    diction[b].sort()

    
def bfs(root):
    visited=[]
    q=deque([root])
    while q:
        node=q.popleft()
        visited.append(node)
        print(node,end=' ')
        if node not in diction:
            return
				#이 부분을 이전과 달리 코딩했다.
        for i in diction[node]:
            if i not in visited:
                visited.append(i)
                q.append(i)

v=[]
def dfs(root):
    v.append(root)
    print(root,end=" ")
    if root not in diction:
        return
    for n in diction[root]:
        if n not in v:
            dfs(n)


dfs(n[2])
print()
bfs(n[2])

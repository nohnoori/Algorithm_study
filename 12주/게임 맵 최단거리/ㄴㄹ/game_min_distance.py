from collections import deque
def solution(maps):
    answer=1

    m=len(maps)
    n=len(maps[0])

    vec=[[0,1],[1,0],[0,-1],[-1,0]]
    que=deque([(0,0)])
    check = [[-1]*n for _ in range(m)]
    check[0][0]=1

    while que:
        r,c=que.popleft()
        if r==m-1 and c==n-1:
            break
        for x,y in vec:
            dr=r+x
            dc=c+y
            if -1<dr<m and -1<dc<n:
                if maps[dr][dc] and check[dr][dc]==-1:
                    check[dr][dc] = check[r][c] + 1
                    que.append((dr,dc))

    return check[-1][-1]

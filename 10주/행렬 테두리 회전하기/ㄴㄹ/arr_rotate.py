def solution(rows, columns, queries):
    answer = []
    graph=[]
    idx=0
    small=rows*columns

    for i in range(rows):
        graph.append([])
        for j in range(columns):
            idx+=1
            graph[i].append(idx)

    for q in queries:
        temp=graph[q[0]-1][q[1]-1]
        small=temp

        for x in range(q[0]-1,q[2]-1):
            graph[x][q[1]-1]=graph[x+1][q[1]-1]
            small=min(small,graph[x+1][q[1]-1])

        for y in range(q[1]-1,q[3]-1):
            graph[q[2]-1][y]=graph[q[2]-1][y+1]
            small=min(small,graph[q[2]-1][y+1])

        for x in range(q[2]-1,q[0]-1,-1):
            graph[x][q[3]-1]=graph[x-1][q[3]-1]
            small=min(small,graph[x-1][q[3]-1])

        for y in range(q[3]-1,q[1]-1,-1):
            graph[q[0]-1][y]=graph[q[0]-1][y-1]
            small=min(small,graph[q[0]-1][y-1])

        graph[q[0]-1][q[1]]=temp
        answer.append(small)

    return answer

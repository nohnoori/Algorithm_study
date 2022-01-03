def solution(answers):
    answer = []
    mx=0
    p=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i in range(3):
        n=len(answers)//len(p[i])
        p[i]=p[i]*(n+1)
    
    for i in range(3):
        res=0
        for j in range(len(answers)):
            if answers[j]==p[i][j]:
                res+=1
        if mx<res:
            mx=res
            answer.clear()
            answer.append(i+1)
        elif mx==res:
            answer.append(i+1)
    
    return answer

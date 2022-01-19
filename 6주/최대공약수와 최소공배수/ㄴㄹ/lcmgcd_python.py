def solution(n, m):
    answer=[]
    a,b=n,m
    while b:
        a,b=b,a%b
    answer.append(a)
    answer.append(n*m//a)
    return answer

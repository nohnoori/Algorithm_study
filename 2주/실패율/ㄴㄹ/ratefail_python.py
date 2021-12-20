def solution(N, stages):
    fail={}
    n=len(stages)
    for i in range(1,N+1):
        if n!=0:
            cnt=stages.count(i)
            fail[i]=cnt/n
            n-=cnt
        else:
            fail[i]=0
    return sorted(fail,key=lambda x:fail[x],reverse=True)

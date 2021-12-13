def solution(n, lost, reserve):
    cnt=0

    lo=list(set(lost)-set(reserve))
    re=list(set(reserve)-set(lost))

    n-=len(lo)

    for i in lo:
        if i-1 in re:
            del re[re.index(i-1)]
            cnt+=1
        elif i+1 in re:
            del re[re.index(i+1)]
            cnt+=1

    return n+cnt


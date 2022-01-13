def solution(dartResult):
    answer =[0,0,0]
    bonus=['S','D','T']
    n=len(dartResult)
    an=-1
    for i in range(n):
        a=dartResult[i]
        if a in bonus:
            answer[an]=answer[an]**(bonus.index(a)+1)
        elif a=='*':
            answer[an]*=2
            if an>0:
                answer[an-1]*=2
        elif a=='#':
            answer[an]*=-1
        else:
            if dartResult[i+1].isdigit():
                an+=1
                answer[an]=int(a)
            else:
                if dartResult[i-1].isdigit():

                    answer[an]=answer[an]*10+int(a)
                else:
                    an+=1
                    answer[an]=int(a)
    return sum(answer)

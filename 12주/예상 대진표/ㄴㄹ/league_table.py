import copy
def solution(n,a,b):
    answer = 0
    part=[i for i in range(1,n+1)]
    
    while part:
        win=[]
        answer+=1
        for i in range(0,n,2):
            if [a,b] == [part[i],part[i+1]] or [b,a] == [part[i],part[i+1]]:
                return answer
            if a in [part[i],part[i+1]]:
                win.append(a)
            elif b in [part[i],part[i+1]]:
                win.append(b)
            else:
                win.append(part[i])
        n//=2
        part=copy.deepcopy(win)
    
    return answer+1

def solution(priorities, location):
    answer = 0
    tup=[(i,num) for i,num in enumerate(priorities)]
    
    while len(tup)>1:
        que=tup.pop(0)
				#1보다 큰 조건문을 두면 tup 길이가 2일때 정확히 계산할 수 없음
        if len(tup)>0:
            list_tup=list(map(lambda x:x[1],tup))
            if que[1]<max(list_tup):
                tup.append(que)
            else:
                if que[0]==location:
                    return answer+1
                else:
                    answer+=1
                    
    return answer+1

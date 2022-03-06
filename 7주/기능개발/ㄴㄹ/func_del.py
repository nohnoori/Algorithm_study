def solution(progresses, speeds):
    answer = []
    idx=0
    while idx<len(progresses):
        cnt=0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        if progresses[idx]>=100:
            cnt+=1
            idx+=1
            for j in range(idx,len(progresses)):
                if progresses[j]>=100:
                    cnt+=1
                    idx+=1
                else:
                    break
            answer.append(cnt)
    return answer

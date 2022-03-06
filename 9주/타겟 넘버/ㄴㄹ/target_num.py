def solution(numbers, target):
    answer = []
    
    def recur(num,tar,i,hap):
        if i>=len(num):
            if hap==tar:
                answer.append(hap)
            return
        recur(num,tar,i+1,hap+num[i])
        recur(num,tar,i+1,hap-num[i])
    
    recur(numbers,target,0,0)
    return len(answer)

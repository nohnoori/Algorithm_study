from itertools import permutations
import copy
def solution(expression):
    answer = 0
    arr=[]
    op=['*','+','-']
    idx=0
    for i in range(len(expression)):
        if expression[i] in op:
            arr.append(expression[idx:i])
            arr.append(expression[i])
            idx=i+1
            cnt=0
            for i in op:
                cnt+=expression[idx:].count(i)
            if cnt==0:
                arr.append(expression[idx:])

    per=list(permutations(op,3))
    for i in per:
        arr_temp=copy.deepcopy(arr)
        for j in i[:2]:
            index=list(filter(lambda x:arr_temp[x]==j,range(len(arr_temp))))
            cnt=0
            for k in index:
                k-=cnt
                arr_temp[k-1:k+2]=[str(eval(''.join(arr_temp[k-1:k+2])))]
                cnt+=2
        res=abs(eval(''.join(arr_temp)))
        if res>answer:
            answer=res

    return answer

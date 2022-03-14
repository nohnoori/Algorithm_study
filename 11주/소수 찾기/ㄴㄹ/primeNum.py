from itertools import permutations
def solution(numbers):
    answer = 0
    l=[]
    num=list(numbers)
    
    for i in range(len(num)):
        per=list(permutations(num,i+1))
        l.append(list(map(lambda x:int(''.join(x)),per)))
        
    l=list(filter(lambda x:x!=1 and x!=0,set(sum(l,[]))))

    for n in l:
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                answer+=1
                break

    return len(l)-answer

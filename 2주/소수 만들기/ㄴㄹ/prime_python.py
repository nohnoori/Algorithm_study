from itertools import combinations
import math
def solution(nums):
    answer =0

    per_num=list(combinations(nums,3))
    for i in range(len(per_num)):
        per_num[i]=sum(per_num[i])
        for j in range(2,int(math.sqrt(per_num[i]))+1):
            if per_num[i]%j==0:
                answer+=1
                break

    return len(per_num)-answer

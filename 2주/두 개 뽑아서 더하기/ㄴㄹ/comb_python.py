from itertools import combinations
def solution(numbers):
    answer=[]
    num=list(combinations(numbers,2))

    for i in range(len(num)):
        answer.append(sum(num[i]))

    return sorted(set(answer))

import re
def solution(s):
    answer = []
    s=s[1:-1].split('{')
    li=[]
    fil=re.compile('\d+')
    for i in s:
        li.append(fil.findall(i))
    li.sort(key=len)
    li=li[1:]

    for i in li:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer

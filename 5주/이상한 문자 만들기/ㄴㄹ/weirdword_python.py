def solution(s):
    answer=[]
    word=s.split(' ')
    for i in word:
        temp=''
        for j in range(len(i)):
            if j%2==0:
                temp+=i[j].upper()
            else:
                temp+=i[j].lower()
        answer.append(temp)
    return ' '.join(answer)

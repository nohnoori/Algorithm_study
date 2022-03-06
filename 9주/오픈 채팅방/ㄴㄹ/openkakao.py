def solution(record):
    answer = []
    idx=[]
    user={}

    for i in range(len(record)):
        split=record[i].split(' ')
        if split[0]=='Enter':
            user[split[1]]=split[2]
            idx.append(split[1])
            answer.append('님이 들어왔습니다.')
        elif split[0]=='Leave':
            idx.append(split[1])
            answer.append('님이 나갔습니다.')
        elif split[0]=='Change':
            user[split[1]]=split[2]

    for i in range(len(answer)):
        answer[i]=user[idx[i]]+answer[i]

    return answer

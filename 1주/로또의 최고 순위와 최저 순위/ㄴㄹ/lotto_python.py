def solution(lottos, win_nums):
    answer = []
    cnt=0

    for win in win_nums:
        if win in lottos:
            cnt+=1

    answer.append(7-cnt)
    answer.append(7-cnt-lottos.count(0))

    for i in range(2):
        if answer[i]>=7:
            answer[i]=6

    return sorted(answer)

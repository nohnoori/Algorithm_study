def solution(participant, completion):
    ans=list(set(participant)-set(completion))
    if not ans:
        for i in participant:
            cnt=participant.count(i)
						#cnt>1 없을때는 효율성 실패
            if cnt>1 and cnt>completion.count(i):
                return i
    else:
        return ans[0]

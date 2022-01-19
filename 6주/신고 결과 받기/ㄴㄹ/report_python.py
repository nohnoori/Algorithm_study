def solution(id_list, report, k):
    answer = [0]*len(id_list)
		#딕셔너리를 이용하여 신고당한 사람:신고한 사람으로 만들 예정
    re={i:[] for i in id_list}

		#중복 제거
    report=list(set(report))

		#re딕셔너리에 신고당한 사람: 신고한 사람 형식으로 넣어주기
		#왜냐하면 이후에 for문을 덜 쓰기 위함
    for i in range(len(report)):
        spl=report[i].split()
        re[spl[1]].append(spl[0])

		#딕셔너리의 key,value 이용
		#id_list 순서대로 넣어놨기 때문에 id_list.index() 이용
		#이전에는 안 쪽 for문과 if문의 위치가 바뀌어있었음 
		# => for문 반복 횟수가 더 많아지기 때문에 if문을 먼저 적는 것이 효율성을 높일 수 있음
		#이를 위해서 re의 형식을 신고당한 사람:신고한 사람으로 한 것.
    for key,val in re.items():
        if len(val)>=k:
            for n in val:
                answer[id_list.index(n)]+=1
    return answer

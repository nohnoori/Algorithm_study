from itertools import combinations
import collections
def solution(orders, course):
    answer = []
    for i in course:
				#course 개수에 따른 각 조합의 종류를 넣기 위한 배열
				#즉 course 개수가 달라지면 다시 초기화 해야함
        comb=[]
        for j in orders:
						#3번 예시의 경우에 문자열 순서가 달라져서 다른 조합으로 취급되기 때문에 애초에 정렬을 해줌
            j=''.join(sorted(j))
            comb+=list(combinations(j,i))
				#combinations, 조합의 개수를 딕셔너리로 만들어 줌
        col=collections.Counter(comb)
				#course의 수가 orders에 있는 최대 길이보다 크면 null이기 때문에 null 아닌 경우에만 적용
        if col:
						#Counter로 나온 중복개수가 1이면 안됨
						#문제에 최소 2번 이상있어야 코스 요리로 채택한다고 적혀있음
            if col.most_common(1)[0][1]>1:
								#중복 최대 개수가 여러개인 경우가 있기 때문에 count를 통해 총 몇 개의 최대값이 있는지 확인
                n=list(col.values()).count(col.most_common(1)[0][1])
								#n개의 최대값이 있기 때문에 하나씩 돌아가면서 문자열로 만들어서 answer에 넣어줌
								#('A','B')의 형식으로 들어있기 때문
                answer+=[''.join(col.most_common(n)[i][0]) for i in range(n)]
    return sorted(answer)

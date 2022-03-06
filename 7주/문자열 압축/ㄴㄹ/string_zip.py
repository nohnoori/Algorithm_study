def solution(s):
		#최대 문자열 길이로 초기화 해줌
		#그래야 min 비교가 가능
		answer=10000
		#len(s)//2+1은 적어도 s길이가 2이상이어야 가능하기 때문에 길이 1일 때를 염두하여 +2 해줌
		for n in range(1,len(s)//2+2):
				res=''
				cnt=1
				#단위문자열 초기화
				#1~len(s)//2만큼 길이를 자르기 때문에 매번 초기화 해줘야 함
				temp=s[:n]

				for i in range(n,len(s)+n,n):
						#단위문자열과 다음 문자열이 같은 값이라면 개수 +1
						if temp==s[i:i+n]:
								cnt+=1
						else:
								#1은 문자열에 넣어주지 않음
								if cnt==1:
										res+=temp
								else:
										res+=str(cnt)+temp
								#temp의 쓸모를 다 하면 다음 문자열로 넘어감(이후 문자열도 계산해야하니까)
								temp=s[i:i+n]
								#cnt는 다시 1로 초기화
								cnt=1
								
				answer=min(answer,len(res))
		return answer

n=int(input())
graph=[]
for i in range(n):
	graph.append(input())

#상하좌우
vec_i=[0,0,-1,1]
vec_j=[1,-1,0,0]
cnt=0
answer=[]

def dfs(x,y):
	global cnt
	if x<0 or x>n-1 or y<0 or y>n-1:
		return
	#1인 경우에만 상하좌우 확인해야함
	#주민이 없는 곳에서 상하좌우를 확인해봤자 서로 다른 단지일수 있음
	if graph[x][y]=='1':
		cnt+=1
		#문자열은 중간값 수정이 어려워서 선택한 방법
		graph[x]=graph[x][:y]+'0'+graph[x][y+1:]
		for i in range(4):
			dfs(x+vec_i[i],y+vec_j[i])

#한번 dfs를 호출하면 단지 하나만 탐색함
for x in range(n):
	for y in range(n):
		dfs(x,y)
		if cnt!=0:
			answer.append(cnt)
			cnt=0

print(len(answer))
#오름차순 출력
answer.sort()
for i in range(len(answer)):
    print(answer[i],end='\n')

node=int(input())
n=int(input())
graph=[[0]*node for i in range(node)]
for i in range(n):
	a,b=map(int,input().split(' '))
	graph[a-1][b-1]=1
	graph[b-1][a-1]=1

visited=[]
def dfs(root):
	visited.append(root)
	for i in range(node):
		if graph[root][i] and i not in visited:
			dfs(i)
	return

dfs(0)
print(len(visited)-1)

n=int(input())
tree=[]
for i in range(n):
	tree.append(input().split(' '))
    
def index(node):
    for i in range(len(tree)):
        if tree[i][0]==node:
            return i

def pre(node):
    idx=index(node)
    print(tree[idx][0],end='')
    if tree[idx][1]!='.':
        pre(tree[idx][1])
    if tree[idx][2]!='.':
        pre(tree[idx][2])

def inorder(node):
    idx=index(node)
    if tree[idx][1]!='.':
        inorder(tree[idx][1])
    print(tree[idx][0],end='')
    if tree[idx][2]!='.':
        inorder(tree[idx][2])

def post(node):
    idx=index(node)
    if tree[idx][1]!='.':
        post(tree[idx][1])
    if tree[idx][2]!='.':
        post(tree[idx][2])
    print(tree[idx][0],end='')

pre('A')
print()
inorder('A')
print()
post('A')

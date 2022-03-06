def seperate(p):
    left=0
    right=0
    r=True
    ans=''
    u=''
    v=''

    if not p:
        return p

		#u,v 분리 작업
    for i in range(len(p)):
        if p[i]=='(':
            left+=1
        elif p[i]==')':
            right+=1

        if right>left:
            r=False

        if left==right:
            u=p[:i+1]
            v=p[i+1:]
            break

		#3,4번 처리
    if r:
        ans=seperate(v)
        return u+ans
    else:
        ans=seperate(v)
        temp='('+ans+')'
        u=u[1:-1]
        for i in range(len(u)):
            if u[i]==')':
                u=u[:i]+'('+u[i+1:]
            else:
                u=u[:i]+')'+u[i+1:]
        return temp+u

def solution(p):
    answer = ''

    if not p:
        return p

    answer=seperate(p)

    return answer

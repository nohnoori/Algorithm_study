def solution(n):
    st=''
    while n>0:
        n,m=divmod(n,3)
        st+=str(m)

    return int(st,3)

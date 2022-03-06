def solution(n):
    mod = ''
    while n>0:
        if n%3!=0:
            mod+=str(n%3)
            n=n//3
        else:
            mod+='4'
            n=n//3-1
    return mod[::-1]

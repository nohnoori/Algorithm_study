def solution(n):
    s='수박'
    a,b=divmod(n,2)

    return s*a+s[:b]

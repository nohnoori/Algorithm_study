def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=i
        else:
            ac=ord(i)+n
            if ac>90 and i.isupper():
                answer+=chr(ac-90+64)
            elif ac>122 and i.islower():
                answer+=chr(ac-122+96)
            else:
                answer+=chr(ac)
    return answer

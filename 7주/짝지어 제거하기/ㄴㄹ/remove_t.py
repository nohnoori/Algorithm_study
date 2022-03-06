def solution(s):
    answer = -1
    stack=[s[0]]

    for i in range(1,len(s)):
        if len(stack)!=0 and stack[-1]==s[i]:
            stack.pop(-1)
        else:
            stack.append(s[i])
    return 1 if len(stack)==0 else 0

def solution(x):
    ha=list(map(int,list(str(x))))
    if x%sum(ha)==0:
        return True
    else:
        return False

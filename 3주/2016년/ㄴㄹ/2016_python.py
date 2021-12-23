def solution(a, b):
    week=['THU','FRI','SAT','SUN','MON','TUE','WED']
    day={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    d=0
    for i in range(1,a):
        d+=day[i]
    return week[(d+b)%7]

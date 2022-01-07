def solution(price, money, count):
    pr=0
    for i in range(1,count+1):
        pr+=price*i
        
    if money<pr:
        return pr-money
    else:
        return 0

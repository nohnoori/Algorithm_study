from math import gcd
def solution(w,h):
    answer = 1
    
    return w*h-(w+h-gcd(w,h))

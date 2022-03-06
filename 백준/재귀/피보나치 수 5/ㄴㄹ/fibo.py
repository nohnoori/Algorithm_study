n=int(input())

def fibo(n):
    if n>1:
        return fibo(n-1)+fibo(n-2)
    else:
        return n
    
print(fibo(n))

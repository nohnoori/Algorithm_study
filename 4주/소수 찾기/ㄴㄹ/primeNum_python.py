def solution(n):
    cnt=0
    arr=[True]*(n+1)
    for j in range(2,n+1):
        if arr[j]==True:
            k=2
            while(j*k)<=n:
                arr[j*k]=False
                k+=1
    return arr.count(True)-2

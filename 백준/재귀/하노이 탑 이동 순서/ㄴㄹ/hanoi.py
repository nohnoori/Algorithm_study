n=int(input())
move=[]
def hanoi(pan,a,b,c):
    if pan==1:
        move.append([a,c])
    else:
        hanoi(pan-1,a,c,b)
        move.append([a,c])
        hanoi(pan-1,b,a,c)

hanoi(n,1,2,3)

print(len(move))
for i in range(len(move)):
    print(move[i][0],move[i][1])

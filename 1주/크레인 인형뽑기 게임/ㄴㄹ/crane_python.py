
def solution(board, moves):
    answer = []
    cnt=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                answer.append(board[j][i-1])
                board[j][i-1]=0
                break
        if len(answer)>1 and answer[-1]==answer[-2]:
            cnt+=2
            del answer[-2:]
    return cnt

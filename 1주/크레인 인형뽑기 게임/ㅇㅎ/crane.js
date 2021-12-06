function solution(board, moves) {
    let bucket = [];
    let cnt = 0;

    for (let i = 0; i < moves.length; i++) {
        const doll = grapDoll(board, moves[i] - 1);
        if (doll) {
            if (bucket[bucket.length - 1] === doll) {
                bucket.pop();
                cnt += 2;
            } else {
                bucket.push(doll)
            }
        }
    }
    return cnt;
}

function grapDoll(board, order) {
    for (let i = 0; i < board.length; i++) {
        if (board[i][order] != 0) {
            const doll = board[i][order];
            board[i][order] = 0;
            return doll;
        }
    }
}
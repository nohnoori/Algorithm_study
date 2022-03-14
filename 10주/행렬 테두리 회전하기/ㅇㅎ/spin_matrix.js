function solution(rows, columns, queries) {
    /* 초기 행렬 생성 */
    let metrix = [];
    for(let r=1; r<=rows; r++){
        let row = [];
        for(let c=1; c<=columns; c++){
            row.push((r-1)*columns+c);
        }
        metrix.push(row);
    }
    /* 쿼리 진행 */
    let mins = [];
    queries.forEach(x => {
        let [x1, y1, x2, y2] = x.map(v => v-1);
        let stack = [];
        for(let i=y1; i<y2; i++) stack.push(metrix[x1][i]);
        for(let i=x1; i<x2; i++) stack.push(metrix[i][y2]);
        for(let i=y2; i>y1; i--) stack.push(metrix[x2][i]);
        for(let i=x2; i>x1; i--) stack.push(metrix[i][y1]);
        
        mins.push(Math.min(...stack));
        let last = stack.pop();
        stack.unshift(last);
        
        for(let i=y1; i<y2; i++) metrix[x1][i] = stack.shift();
        for(let i=x1; i<x2; i++) metrix[i][y2] = stack.shift();
        for(let i=y2; i>y1; i--) metrix[x2][i] = stack.shift();
        for(let i=x2; i>x1; i--) metrix[i][y1] = stack.shift();
    })
    return mins;
}

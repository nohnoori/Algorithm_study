function solution(d, budget) {
    let dSort = d.sort((a,b) => a - b);
    let cnt = 0;
    let tmp = 0;
    for(let i=0; i< d.length; i++){
        if(tmp + d[i] > budget) return cnt;
        tmp += d[i];
        cnt += 1;
    }
    return cnt;
}

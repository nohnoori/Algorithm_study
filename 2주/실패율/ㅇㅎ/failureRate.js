function solution(N, stages) {
    let result = [];
    for(let i=1; i<=N; i++){
        let [reach, clear] = [0, 0];
        stages.forEach(stage => {
            if(i == stage) reach += 1;
            if(i <= stage) clear += 1;
        })
        result.push([i, reach/clear]);
    }
    result.sort((a,b) => b[1] - a[1]);
    return result.map(x => x[0]);
}

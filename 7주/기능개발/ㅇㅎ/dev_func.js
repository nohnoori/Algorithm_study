// 최대 0.15ms
function solution(progresses, speeds) {
    let day = progresses.map((x,i) => Math.ceil((100-x)/speeds[i]));
    let result = [1];
    let idx = 0;
    for(let i=1; i<day.length; i++){
        let last = result.length-1;
        if(day[idx] >= day[i]){
            result[last] += 1;
        } else {
            idx = i;
            result[last+1] = 1;
        }
    }
    return result;
}

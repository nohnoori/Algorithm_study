// 최대 : 3.84ms
function solution(sizes) {
    let max = [0, 0]; // w, h
    for(let i=0; i<sizes.length; i++){
        if(sizes[i][0] < sizes[i][1]){
            max[0] = max[0] < sizes[i][1] ? sizes[i][1] : max[0];
            max[1] = max[1] < sizes[i][0] ? sizes[i][0] : max[1];
        } else {
            max[0] = max[0] < sizes[i][0] ? sizes[i][0] : max[0];
            max[1] = max[1] < sizes[i][1] ? sizes[i][1] : max[1];
        }
    }
    return max[0] * max[1];
}

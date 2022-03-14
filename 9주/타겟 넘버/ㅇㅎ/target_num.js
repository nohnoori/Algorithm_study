function solution(numbers, target) {
    let cnt = 0;
    
    getNum(0,0);
    function getNum(idx, sum){
        if(idx === numbers.length){
            if(sum === target){
                cnt++;
            }
            return;
        }
        getNum(idx+1, sum+numbers[idx]);
        getNum(idx+1, sum-numbers[idx]);
    }
    return cnt;
}

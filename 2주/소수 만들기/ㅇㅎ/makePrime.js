function solution(nums) {
    let cnt = 0;
    // 서로 다른 세 수 뽑기
    for(let i=0; i < nums.length-2; i++){
        for(let j=i+1; j < nums.length-1; j++){
            for(let k=j+1; k < nums.length; k++){
                let num = nums[i] + nums[j] + nums[k];
                // 소수 판별 -> 소수면 count
                for(let i=2; i<num; i++){
                    if(num % i === 0){
                        break;
                    }
                    if(i === num-1) cnt++;
                }
            }
        }
    }
    return cnt;
}

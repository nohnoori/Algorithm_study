function solution(answers) {
    let supo1 = [1,2,3,4,5];
    let supo2 = [2,1,2,3,2,4,2,5];
    let supo3 = [3,3,1,1,2,2,4,4,5,5];
    let cnt = [0,0,0];
    
    cnt[0] = answers.filter((v,i) => v === supo1[i%supo1.length]).length;
    cnt[1] = answers.filter((v,i) => v === supo2[i%supo2.length]).length;
    cnt[2] = answers.filter((v,i) => v === supo3[i%supo3.length]).length;
    let max = Math.max(...cnt);
    
    let result = [];
    for(let i=0; i<cnt.length; i++){
        if(max == cnt[i]) result.push(i+1);
    }
    return result;
}

function solution(left, right) {
    let result = 0;
    for(let i=left; i<=right; i++){
        let cnt = 1;
        for(let j=1; j < i; j++){
            if(i % j == 0) cnt++;
        }
        result += (cnt % 2 == 0 ? i : i*-1);
    }
    return result;
}

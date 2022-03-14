function solution(n) {
    const num124 = [1, 2, 4];
    let result = "";
    
    while(n > 0){
        result = num124[(n-1)%3] + result;
        n = Math.floor((n-1)/3);
    }
    return result;
}

// 최대 489.22ms
function solution(w, h) {
    let gcd = 1;
    for(let i=2; i<=Math.min(w,h); i++){
        if(w%i==0 && h%i==0) gcd = i;
    }
    return (w*h) - (w+h - gcd);
}

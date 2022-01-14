function solution(n){
    return n.toString().split('').reduce((acc,v) => acc + v*1, 0);
}

function solution(x) {
    return (x % (x+"").split('').reduce((acc,v) => acc + v*1, 0)) == 0 ? true : false;
}

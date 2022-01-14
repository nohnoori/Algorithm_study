function solution(s) {
    let arr = s.split(' ').map(x => x.split('').map((y,i) => i%2==0 ? y.toUpperCase() : y.toLowerCase()));
    return arr.map(x => x.join("")).join(" ");
}

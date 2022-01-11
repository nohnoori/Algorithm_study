// 최대 88ms
function solution(price, money, count) {
    let sum = Array(count).fill().map((_, i) => i+1).reduce((acc,v) => acc + v*price, 0);
    return sum > money ? sum - money : 0;
}

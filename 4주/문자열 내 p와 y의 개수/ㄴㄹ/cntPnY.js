// 최대 13ms
function solution(s){
    let sArr = s.toLowerCase().split('');
    let p = sArr.filter(x => x === 'p').length;
    let y = sArr.filter(x => x === 'y').length;
    return p == y ? true : false;
}

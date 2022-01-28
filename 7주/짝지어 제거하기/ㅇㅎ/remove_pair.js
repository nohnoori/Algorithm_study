// 최대 49.77ms
function solution(s){
    let tmp = [s[0]];
    for(let i=1; i<s.length; i++){
        if(tmp[tmp.length-1] == s[i]){
            tmp.pop();
        } else {
            tmp.push(s[i]);
        }
    }
    return tmp.length ? 0 : 1;
}

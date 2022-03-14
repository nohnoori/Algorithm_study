function solution(p) {
    if(!p.length) return p;
    // 문자열을 균형잡힌 괄호 문자열 u,v로 분리
    function seperateStr(str) {
        let cnt = 0;
        for(let i=0; i<str.length; i++){
            if(str[i] == '(') cnt++;
            if(str[i] == ')') cnt--;
            if(cnt == 0) return [str.slice(0,i+1), str.slice(i+1)];
        }
    }
    let [u, v] = seperateStr(p);
    let recursiveV = solution(v);
    if(u[0] == '(' && u[u.length -1] == ')') {
        return u + recursiveV;
    } else {
        let tmp = '(' + recursiveV + ')';
        let reverseU = u.split('').slice(1, u.length-1).map(x => x == '(' ? ')' : '(').join('');
        return tmp + reverseU;
    }
}

// 최대 6.68ms
function solution(s) {
    let min = s.length;
    for(let i=1; i<=s.length/2; i++){
        let tmp = "";
        let cnt = 1;
        for(let j=0; j<s.length;j+=i){
            if(s.slice(j,j+i) == s.slice(j+i,j+i*2)){
                cnt++;
            } else {
                if(cnt != 1) tmp += cnt;
                tmp += s.slice(j, j+i);
                cnt = 1;
            }
        }
        if(min > tmp.length) min = tmp.length;
    }
    return min;
}

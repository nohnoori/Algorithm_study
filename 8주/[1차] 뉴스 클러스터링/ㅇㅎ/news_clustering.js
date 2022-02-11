function solution(str1, str2) {
    function strFilter(str){
        let arr = [];
        for(let i=0; i<str.length-1; i++){
            let tmp = (str[i] + str[i+1]).toLowerCase();
            if(tmp.match(/[a-z]{2}/)) arr.push(tmp);
        }
        return arr;
    }
    let s1 = strFilter(str1);
    let s2 = strFilter(str2);
    let set = new Set([...s1, ...s2]);
    let union = 0;
    let inter = 0;
    set.forEach(x => {
        let cnt1 = s1.filter(v => v === x).length;
        let cnt2 = s2.filter(v => v === x).length;
        union += Math.max(cnt1, cnt2);
        inter += Math.min(cnt1, cnt2);
    })
    return union != 0 ? Math.floor(inter/union*65536) : 65536;
}

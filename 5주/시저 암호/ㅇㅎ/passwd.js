function solution(s, n) {
    let up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let low = 'abcdefghijklmnopqrstuvwxyz';
    let result = "";
    for(let i=0; i<s.length; i++){
        if(s[i] == ' '){
          result += ' '; 
        } else {
            let check = s[i] == s[i].toUpperCase() ? up : low;
            result += check[(check.indexOf(s[i]) + n) % 26]
        }
    }
    return result;
}

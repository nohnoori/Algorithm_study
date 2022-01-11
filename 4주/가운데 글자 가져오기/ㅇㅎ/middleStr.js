function solution(s) {
    let len = s.length;
    return len % 2 != 0 ? s[parseInt(len/2)] : s.substr(len/2-1,2);
}

function solution(s) {
    let lenChk = ![4,6].includes(s.length) ? false : true;
    let numCnt = s.split('').filter(x => !isNaN(x)).length;
    let numChk = s.length === numCnt ? true : false;
    return lenChk && numChk;
}

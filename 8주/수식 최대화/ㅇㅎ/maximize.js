function solution(expression) {
    function getCase(arr, select){
        let result = [];
        if(select==1){
            return arr;
        }
        arr.forEach((fix, idx, origin) => {
            let rest = [...origin.slice(0,idx), ...origin.slice(idx+1,)];
            let tmp = getCase(rest, select-1);
            let attached = tmp.map(x => [fix, ...x]);
            result.push(...attached);
        })
        return result;
    }
    let op = expression.match(/[+\-\*]/gi);
    let opSet = [...new Set(op)];
    let num = expression.match(/\d{1,}/g).map(x => parseInt(x));
    let cases = getCase(opSet, opSet.length);
    let max = 0;
    for(let i=0; i<cases.length; i++){
        let copyOp = op.slice();
        let copyNum = num.slice();
        for(let j=0; j<cases[i].length; j++){
            for(let k=0; k<copyOp.length; k++){
                if(cases[i][j] == copyOp[k]){
                    if(copyOp[k] == '*'){
                        copyNum[k] *= copyNum[k+1];
                    } else if (copyOp[k] == '+'){
                        copyNum[k] += copyNum[k+1];
                    } else if (copyOp[k] == '-'){
                        copyNum[k] -= copyNum[k+1];
                    }
                    copyNum.splice(k+1,1);
                    copyOp.splice(k,1);
                    k--;
                }
            }
        }
        let result = Math.abs(copyNum[0]);
        if(max < result) max = result;
    }
    return max;
}

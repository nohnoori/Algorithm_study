function solution(dartResult) {
    let sdt = ['S','D','T'];
    let result = [];
    for(let i=0; i<dartResult.length; i++){
        let curr = dartResult[i];
        let last = result.length-1;
        if(!isNaN(curr)){
            if(curr == 0 && dartResult[i-1] == 1){
                result[last] *= 10;
            } else {
                result.push(curr*1);
            }
        } else if(sdt.includes(curr)){
            result[last] **= sdt.indexOf(curr)+1;
        } else if(['#','*'].includes(curr)){
            let prize = curr == '*' ? 2 : -1;
            if(prize == 2 && result.length != 1) {
                result[last-1] *= prize;
            }
            result[last] *= prize;
        }
    }
    return result.reduce((acc,v) => acc+v, 0);
}

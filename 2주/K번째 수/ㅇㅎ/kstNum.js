function solution(array, commands) {
    let result = [];
    commands.forEach( c => {
        let tmp = array;
        result.push(tmp.slice(c[0]-1, c[1]).sort((a,b)=>a-b)[c[2]-1]);
    })
    return result;
}

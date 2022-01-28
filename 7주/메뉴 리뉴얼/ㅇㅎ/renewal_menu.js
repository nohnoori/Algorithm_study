// 최대 7.42ms
function solution(orders, course) {
    let answer = [];
    for(let i=0; i < course.length; i++){
        const size = course[i];
        const map = new Map();
        
        for(let j=0; j<orders.length; j++){
            const order = orders[j].split('').sort().join('');
            combination(size, map, order, 0, "", 0);
        }
        getMaxSet(map, answer);
    }
    return answer.sort();
}

function combination(n, map, order, r, str, start) {
    if(n==r) {
        if(map.get(str)){
            map.set(str, map.get(str) + 1);
        } else {
            map.set(str, 1);
        }
        return;
    }
    for(let i=start; i<order.length; i++){
        let ch = order.charAt(i);
        combination(n, map, order, r+1, str+ch, i+1);
    }
}

function getMaxSet(map, answer){
    let max = Math.max(...map.values());
    for(let [key, value] of map){
        if(max === value && max != 1) {
            answer.push(key);
        }
    }
}

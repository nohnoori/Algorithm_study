function solution(s) {
    let result = [];
    let sets = s.slice(2,-2).split('},{').sort((a,b) => a.length - b.length);
    sets.forEach(set => {
        let elements = set.split(',');
        for(let i=0; i<elements.length; i++){
            let num = elements[i]*1
            if(!result.includes(num)) result.push(num);
        }
    })
    return result;
}

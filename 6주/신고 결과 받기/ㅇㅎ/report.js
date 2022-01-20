function solution(id_list, report, k) {
    let new_report = [...new Set(report)].map(x => x.split(' '));
    let dic = {};
    new_report.forEach(x => {
        let itIn = dic[x[1]];
        itIn ? itIn.push(x[0]) : dic[x[1]] = [x[0]];
    })
    let result = Array(id_list.length).fill(0);
    for(var i in dic){
        if(dic[i].length >= k){
            dic[i].forEach(x => {
                result[id_list.indexOf(x)]++;
            })
        }
    }
    return result;
}

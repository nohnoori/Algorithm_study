function solution(n, lost, reserve) {
    let real_reserve = reserve.filter(x=> !lost.includes(x)).sort((a,b) => a-b);
    let real_lost = lost.filter(x=> !reserve.includes(x)).sort((a,b) => a-b);
    
    for(let i=0; i<real_reserve.length; i++){
        if(real_lost.includes(real_reserve[i]-1)){
            real_lost = real_lost.filter(x => x != real_reserve[i]-1);
            continue;
        } else if(real_lost.includes(real_reserve[i]+1)){
            real_lost = real_lost.filter(x => x != real_reserve[i]+1);
            continue;
        }
    }
    return n - real_lost.length;
}

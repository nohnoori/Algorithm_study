function solution(a, b) {
    let month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let day = ['FRI','SAT','SUN','MON','TUE','WED','THU'];
    let date = b-1;
    
    for(let i=0; i<a-1; i++){
        date += month[i];
    }
    
    return day[date%7];
}

function solution(priorities, location) {
    let cnt = 0;
    while(true){
        let len = priorities.length;
        function checkPriority(){
            for(let i=1; i<len; i++){
                if(priorities[0] < priorities[i]) return false;
            }
            return true;
        }
        let ok = checkPriority();
        if(ok){
            cnt++;
            priorities.shift();
            if(location == 0) return cnt;
        } else {
            let tmp = priorities.shift();
            priorities.push(tmp);
        }
        location -= location == 0 ? (len-1)*-1 : 1;
    }
}

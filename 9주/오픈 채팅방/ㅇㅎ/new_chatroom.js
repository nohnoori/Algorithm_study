function solution(record) {
    let result = [];
    let user = {};
    let states = [];
    const stateMsgs = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }
    
    record.forEach(msg => {
        let [state, id, nick] = msg.split(' ');
        
        if(state != 'Change')
            states.push([id, state]);
        if(nick)
            user[id] = nick;
    })
    
    states.forEach(x => {
        result.push(`${user[x[0]]}${stateMsgs[x[1]]}`);
    })
    return result;
}

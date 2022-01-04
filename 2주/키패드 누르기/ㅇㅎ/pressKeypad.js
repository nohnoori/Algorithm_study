function solution(numbers, hand) {
    let myHand = hand === "left" ? ["L", 0] : ["R", 1];
    let result = "";
    const keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3,2]
    }
    let loc = [keypad["*"],keypad["#"]];
    numbers.forEach(n => {
        if(![2,5,8,0].includes(n)){
            if([1,4,7].includes(n)){
                result += "L";
                loc[0] = keypad[n];
            } else {
                result += "R";
                loc[1] = keypad[n];
            }
        } else {
            let dist_L = getDistance(loc[0], keypad[n]);
            let dist_R = getDistance(loc[1], keypad[n]);
            if(dist_L < dist_R) {
                result += "L";
                loc[0] = keypad[n];
            } else if (dist_L > dist_R) {
                result += "R";
                loc[1] = keypad[n];
            } else {
                result += myHand[0];
                loc[myHand[1]] = keypad[n];
            }
        }
    })
    return result;
}
function getDistance(loc, target){
    let x = Math.max(loc[0], target[0]) - Math.min(loc[0], target[0]);
    let y = Math.max(loc[1], target[1]) - Math.min(loc[1], target[1]);
    return x+y;
}

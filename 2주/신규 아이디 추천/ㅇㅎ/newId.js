function solution(new_id) {
    let answer = new_id.toLowerCase()
                     .replace(/[^a-z0-9-_.]/g, "")
                     .replace(/\.{1,}/g, ".")
                     .replace(/^\.|\.$/, "")
                     .replace(/^$/, "a")
                     .slice(0,15)
                     .replace(/\.$/, "");
    let len = answer.length; 
    return len > 2 ? answer : answer + answer.charAt(len-1).repeat(3-len);
}

function solution(numbers) {
    let result = numbers.map(v => v+"").sort((a,b) => (b+a)*1 - (a+b)*1).join("");
    return result+0 == 0 ? "0" : result;
}

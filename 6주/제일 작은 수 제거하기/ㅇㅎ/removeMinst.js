function solution(arr) {
    let min = Math.min(...arr);
    let result = arr.filter(x => x != min);
    return result.length ? result : [-1];
}

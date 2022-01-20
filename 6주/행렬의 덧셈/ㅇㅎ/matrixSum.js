// 최대 7.31ms
function solution(arr1, arr2) {
    return arr1.map((a,i) => a.map((_,j) => arr1[i][j] + arr2[i][j]));
}

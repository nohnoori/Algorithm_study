function solution(n, arr1, arr2) {
    let a1 = arr1.map(v => v.toString(2).padStart(n,0));
    let a2 = arr2.map(v => v.toString(2).padStart(n,0));
    let a3 = a1.map((_,i) => a1[i].split('').map((_,j)=> a1[i][j] | a2[i][j]));
    let result = a3.map((_,i) => a3[i].map((_,j) => a3[i][j] == 1 ? "#" : " "));
    return result.map(x => x.join(""));
}

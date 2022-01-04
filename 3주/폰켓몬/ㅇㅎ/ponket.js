function solution(nums) {
    let need = nums.length/2;
    let max = [...new Set(nums)].length;
    return max > need ? need : max;
}

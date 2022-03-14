function solution(numbers) {
    let cnt = 0;
    let nums = numbers.split('');
    let set = new Set();
    makeNum(nums, "")
     0 [1,1]  

    function makeNum(arr, str){
        if(str.length > 0){
            let num = str*1;
            if(!set.has(num)) {
                set.add(num);
                if(isPrime(num)){
                    cnt++;
                }
            }
        }
        if(arr.length > 0){
            for(let i=0; i<arr.length; i++){
                let t = arr.slice();
                t.splice(i,1);
                makeNum(t, str+arr[i]);
            }
        }
    }
    function isPrime(num){
        if(num < 2) return false;
        if(num % 2 === 0 && num != 2) return false;
        for(let i=3; i<=Math.sqrt(num); i++){
            if(num%i === 0) return false;
        }
        return true;
    }
    return cnt;
}

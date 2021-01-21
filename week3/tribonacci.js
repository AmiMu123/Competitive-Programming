// O(n) time
// space O(1) space
/**
 * @param {number} n
 * @return {number}
 */
// iterative approach
var tribonacci = function(n) {
    if(n ===0){
 
         return 0;
 }
     if(n <3){
         return 1;
 }
     let j = 0; k = 1;m = 1;
     let sum = 0;
     for(let i = 2;i<n ;i++){
         sum = j + k + m;
         j = k;
         k = m;
         m = sum;
 
 }
     return sum;
    
 };

 // recurssive approach
 // time complexity  O(n)
 
 /**
 * @param {number} n
 * @return {number}
 */
let cache = new Map();
var tribonacci = function(n) {
   if(n ===0){
        return 0;
    }
    if(n <3){
        return 1;
    }
    
    
        if(cache.has(n)){
            return cache(n)
        }

        var ans = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        cache[n] = ans;
        return ans;
};
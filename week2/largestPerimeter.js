/**
 * @param {number[]} A
 * @return {number}
 */

 // time complexity = O(n)  
 // space complexity = O(1);
var largestPerimeter = function(A) {
    let sortedA = A.sort(function(b,a){return (b-a)});
       len = sortedA.length;
       for(let i = len -1;i>=0;i--){
           let c = sortedA[i];
           let b = sortedA[i-1];
           let a = sortedA[i-2];
           if(c <a + b){
               return a + b +c;
   }
   }
       return 0;
       };
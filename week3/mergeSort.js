/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    //check whether the array can be splitted or not
     if(nums.length <2){
         return nums;
 }
     let mid = Math.floor(nums.length/2);
     let left = nums.slice(0,mid);
     let right = nums.slice(mid,nums.length);
     return merge(sortArray(left), sortArray(right))
 
 };
 
 // left and right are sorted arrays
 var merge = function(left,right){
     let result = []
     
     while(left.length && right.length){
         if(left[0] <= right[0]){
             result.push(left.shift())
         
 
             }
         else{
             result.push(right.shift())
 }
 }
     while(left.length){
         result.push(left.shift());
 }
     while(right.length){
         result.push(right.shift())
 }
     return result;
     
 }
 console.log(sortArray([3,1,4,5,0,2]))
 
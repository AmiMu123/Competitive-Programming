/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(let i = 0;i<nums.length;i++){
        nums.sort(function(a,b){return a-b})
}
    return nums;
};
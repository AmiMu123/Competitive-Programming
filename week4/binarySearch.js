/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    // iterative approach
    // while(left <= right){
    //     let mid = Math.floor((right + left)/2);
    //     if(nums[mid] === target){
    //         return mid;
    //     }
    //     else if(nums[mid] < target){
    //         left = mid + 1;
    //     }
    //     else if(nums[mid] > target){
    //         right = mid-1
    //     }
    // }
//     if(left <=right){
//         let mid = Math.floor((right + left)/2);
        
//     }
//     return -1
    return helper(left,right,nums,target);
};

// recursive approach 
let helper = (left,right,nums,target) =>{
    if(left >right){
        return -1
    }
    let mid = Math.floor((right + left)/2);
    if(nums[mid] === target){
        return mid
    }
    else if(nums[mid] > target){
        return helper(left,mid-1,nums,target)
    }
    else{
        return helper(mid+1,right,nums,target);
    }
    
    
}
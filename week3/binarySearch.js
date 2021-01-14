/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length -1; // 5;
    // time compleixty = O(log n) space complexity = O(1) space 
    while(left <=right){
        let mid = Math.floor((left + right)/2);
        if(target>nums[mid]){
            left = mid + 1;

}
        else if(target <nums[mid]){
            right = mid -1;
}
        else{
                return mid;

            }
                    
}
    return -1;
    
        
};

console.log(search([-1,0,3,5,9,12],
    9))
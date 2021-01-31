/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    let count = 0;
    for(let i = 0;i<nums.length ; i++){
        if(nums[i] > nums[i+1]){
            if(i > 0){                
                if(nums[i+1] >=nums[i-1]){
                    nums[i] = nums[i-1]                    
                }
                else{
                    nums[i+1] = nums[i]
                    
                }
            }
            count++;
        }
    }
    return count <=1;
};

console.log(checkPossibility([4,2,1]))
console.log(checkPossibility([3,4,2,3]))

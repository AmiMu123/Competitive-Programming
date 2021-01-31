/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var constructMaximumBinaryTree = function(nums) {
    if(nums.length ===0){
      return null;
  } 
   if(nums.length === 1){
       return new TreeNode(nums[0])
   }
   let indexOfmax = findMax(nums);
   let max = nums[indexOfmax];
   let t = new TreeNode(max);
   t.left = constructMaximumBinaryTree(nums.slice(0,indexOfmax))
   t.right = constructMaximumBinaryTree(nums.slice(indexOfmax+1,nums.length))
   return t;
};

let findMax = (nums) =>{
   let indexOfmax = 0;
   for(let i = 0;i<nums.length;i++){
       if(nums[i] > nums[indexOfmax]){
           indexOfmax = i;
       }
   }
       return indexOfmax;
   
}

 
   



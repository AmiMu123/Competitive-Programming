/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    let sum = 0;
    let sortedArray = []
    checker(root,sortedArray);
    for(let i = 0;i<sortedArray.length;i++){
        if(sortedArray[i] >=low && sortedArray[i] <=high){
            sum = sum + sortedArray[i];
        }
    }
    return sum;
};

let checker = function(root,sortedArray){
    if(root !==null){
        checker(root.left,sortedArray);
        sortedArray.push(root.val);
        checker(root.right,sortedArray);
    }
}

        
    
    



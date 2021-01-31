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
 * @return {number}
 */
var minDiffInBST = function(root) {
    let res = [];
    helper(root,res);
    let min = Math.abs(res[0] - res[1])
    for(let i = 0;i<res.length;i++){
        min = Math.abs(res[i] - res[i+1]) < min ? Math.abs(res[i] - res[i+1]) : min;
    }
        return min;
    
};
let helper = (root,res) =>{
    if(root!==null){
        helper(root.left,res);
        res.push(root.val);
        helper(root.right,res);
    }
    return res;
}
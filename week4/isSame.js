/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    return isSame(p,q);
};

let isSame = (p,q) =>{
    if(p ===null && q ===null){
        return true;
    }
    if(q ==null || p ==null){
        return false;
    } 
    if(p.val !== q.val){
        return false;
    }
    
    let left = isSame(p.left,q.left) 
    let right= isSame(p.right,q.right);
    return left && right;
    
    // return isSame(p.left,q.left) && isSame(p.right,q.right);
    

    
}
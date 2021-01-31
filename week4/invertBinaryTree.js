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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    return invert(root);
};

let invert = (r) =>{
    let temp;
    if(r !==null){
        temp = r.left;
        r.left = r.right;
        r.right = temp
        invert(r.left);
        invert(r.right);
    }
    return r;
}

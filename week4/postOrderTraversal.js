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
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    let array = []
    return pod(root,array);
};

let pod = (root,array) =>{
    if(root !==null){
        
        pod(root.left,array);
        pod(root.right,array);
        array.push(root.val);
        
    }
    return array;
    
}
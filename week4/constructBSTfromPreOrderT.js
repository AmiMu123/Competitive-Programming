/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function(preorder) {
    let t = new TreeNode(preorder[0])
    let ans;
    for(let i = 1;i < preorder.length;i++){
        res = preorder[i]
         ans =  bst(t,res)
    }
    return ans;
}

var bst = function(node,val) {
    if(node ===null){
        return new TreeNode(val)
    }
    if(node.val > val){
        node.left = bst(node.left,val)
    }
    else if(node.val < val){
        node.right = bst(node.right,val)
    }
    else{
        return node;
    }
    return node
    
}

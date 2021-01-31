
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    return isSym(root,root);
};

let isSym = (p,q) =>{
    if(p ===null && q ===null){
        return;
    }
    if(q ==null || p ==null){
        return;
    } 
    let left  = isSym(p.left,q.right) 
    let right = isSym(p.right,q.left);
    return left && right;
}


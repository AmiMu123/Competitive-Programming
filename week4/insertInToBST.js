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
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    let newNode = new TreeNode(val);
    if(root ===null){
        root = newNode;
        return root;
  }
    // iterative approach
//     else{
//         let curr = root;
//         while(curr.left || curr.right){
//             if(curr.val >val){     
//                 if(curr.left){
//                     curr = curr.left;
//                 }
//                 else{
//                     curr.left = newNode;
//                     return root;
//                 }
//             }
//             else{
//                 if(curr.right){
//                     curr = curr.right;
//                 }
//                 else{
//                     curr.right = newNode;
//                     return root;
//                 }
//             }
//         }
//         if(curr.val > val){
//             curr.left = newNode;
//         }
//         else{
//             curr.right = newNode;
//         }
        
    
//     return root;
    
    
// }
    
       // recurssive approach 
       if(root !==null){
           if(val > root.val){
               if(root.right){
                  insertIntoBST(root.right,val); 
               }
               else{
                   root.right = new TreeNode(val)
               }
           }
           else{
               if(root.left){
                   insertIntoBST(root.left,val)
               }
               else{
                   root.left = new TreeNode(val)
               }
           }
       }
            
        return root;
    }



    




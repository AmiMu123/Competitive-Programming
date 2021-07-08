# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.node_list = []
        self.inorder(root)
        self.index = 0
        
    def next(self) -> int:
            self.index += 1
            return self.node_list[self.index-1]
        
        
    def hasNext(self) -> bool:
        return self.index < len(self.node_list)
        
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            self.node_list.append(node.val)
            self.inorder(node.right)
            
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
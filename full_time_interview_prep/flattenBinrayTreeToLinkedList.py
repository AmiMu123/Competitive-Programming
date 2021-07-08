# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.flattenTree(root)
    
    def flattenTree(self,node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        
        last_right = self.flattenTree(node.right)
        last_left = self.flattenTree(node.left)
        
        if last_right and last_left:
            temp = node.right
            node.right = node.left
            last_left.right = temp
        elif last_left:
            node.right = node.left
            last_right = last_left
        
        node.left = None
        return last_right
        
            
        
        
        
#         arr = []
#         self.preord(root,arr)
#         print(arr)
#         for i in range(1,len(arr)):
#             arr[i-1].right = arr[i]
#             arr[i-1].left = None
#             arr[i].left = None
#         return root
            
            
            
        
    
    # def preord(self,node,arr):
    #     if node:
    #         arr.append(node)
    #         self.preord(node.left,arr)
    #         self.preord(node.right,arr)

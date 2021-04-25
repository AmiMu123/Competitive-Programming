# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
        arr = []
        sum = []
        sum.append(node.val)
        
        leafNode : 
            sum.append(node.val) [4,9,5]
            arr.append("".join(sum)) ,arr = ["495"]
        dfs(left)
        dfs(right)
        sum.pop()
        
        
        
        
"""
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        container = []
        total = 0
        self.dfs(root,container,[])
        for i in container:
            total += int(i)
        return total
    def dfs(self,node,container,arr):
        if node:
            arr.append(str(node.val))
            if not node.left and not node.right:
                container.append("".join(arr))
            self.dfs(node.left,container,arr)
            self.dfs(node.right,container,arr)
            arr.pop()
            
            

            
        
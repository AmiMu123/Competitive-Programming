# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            result = [root.val]
        queue = deque([(root)])
        while queue:
            arr = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(queue)):
                arr.append(queue[i].val)
            if len(arr) != 0:
                result.append(max(arr))
        return result
            
                   
            
            
        
                
        
                
                
        
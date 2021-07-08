# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root,0)])
        max_width = 0
        while queue:                       
            l = len(queue)
            min_index = float(inf)
            max_index = 0
            for _ in range(l):
                curr = queue.popleft()
                min_index = min(min_index,curr[1])
                max_index = max(max_index,curr[1])
                if curr[0].left:
                    queue.append((curr[0].left,curr[1] * 2))
                if curr[0].right:
                    queue.append((curr[0].right,curr[1]*2 + 1))
            max_width =  max(max_width,max_index-min_index + 1)
        return max_width
                
                    
            
                       
                       
            
        
        
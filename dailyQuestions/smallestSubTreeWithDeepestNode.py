# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
given :
    root of , the depth of each node is --> the shortest distannce to the root
        return -- the smallest subtree such that it contains all the deepest nodes in the original tree
        
"""

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None
            left = dfs(node.left)
            right = dfs(node.right)
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            elif left[0] < right[0]:
                return right[0] + 1,right[1]
            else:
                return left[0] + 1,node
            
        return dfs(root)[1]
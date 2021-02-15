# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, lev = queue.popleft()
            if not node.left and not node.right:
                return lev
            if node.left:
                queue.append((node.left, lev + 1))
            if node.right:
                queue.append((node.right, lev + 1))

        # return self.dfs(root)
#     def dfs(self,node) :
#         if node == None:
#             return 0
#         if self.isLeaf(node):
#             return 1
#         if node.left and node.right:
#             left = self.dfs(node.left)
#             right = self.dfs(node.right)
#             return min(left,right) + 1

#         if node.right :
#             return self.dfs(node.right) + 1
#         if node.left :
#             return self.dfs(node.left) + 1

#     def isLeaf(self,node):
#         return (not node.left and not node.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        result = []
        level_sum = 0
        if queue is None or root is None:
            return []
        while queue:
            level_sum = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / size)
        return result

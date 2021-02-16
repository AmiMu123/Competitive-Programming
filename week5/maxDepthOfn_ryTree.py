"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# from collections import deque


class Solution:
    def maxDepth(self, root: 'Node'):
        if not root:
            return 0
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1

        # bfs solution
#         queue = deque()
#         queue.append(root)
#         level = 0
#         while queue:
#             size = len(queue)
#             for i in range(size):
#                 node =queue.popleft()
#                 for j in range(len(node.children)):
#                     queue.append(node.children[j])
#             level += 1
#         return level

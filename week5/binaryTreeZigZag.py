# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        level = 0

        res = [[root.val]]
        while queue:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            level += 1
            if not queue:
                break
            if level % 2 == 0:
                arr = []
                for i in range(len(queue)):
                    arr.append(queue[i].val)
                res.append(arr)
            else:
                arr = []
                for i in range(len(queue)-1, -1, -1):
                    arr.append(queue[i].val)
                res.append(arr)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root):
        total = [0]
        if not root:
            return 0
        self.dfs(root, 1, total)
        return total[0]

    def dfs(self, node, parentVal, total):
        if node.left:
            if parentVal % 2 == 0:
                total[0] += node.left.val
            self.dfs(node.left, node.val, total)
        if node.right:
            if parentVal % 2 == 0:
                total[0] += node.right.val
            self.dfs(node.right, node.val, total)
        return total

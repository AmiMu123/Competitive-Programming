# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        summ = [0]
        res = []
        self.dfs(root, targetSum, summ, res)
        for i in res:
            if i == targetSum:
                return True
        return False

    def dfs(self, node, target, summ, res):
        if not node:
            return 0
        if not node.left and not node.right:
            summ[0] += node.val
            res.append(summ[0])

        if node.left:
            self.dfs(node.left, target, [summ[0]+node.val], res)
        if node.right:
            self.dfs(node.right, target, [summ[0]+node.val], res)

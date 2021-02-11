# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = [0]
        self.helper(root, ans)
        return ans[0]

    def helper(self, node, ans):
        if not node:
            return 0
        left = self.helper(node.left, ans)
        right = self.helper(node.right, ans)
        rightMax = 0
        leftMax = 0

        if node.left and node.left.val == node.val:
            leftMax += left + 1
        if node.right and node.right.val == node.val:
            rightMax += right + 1
        ans[0] = max(ans[0], rightMax + leftMax)
        return max(rightMax, leftMax)

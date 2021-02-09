# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return (0, 0)
        if not root.right and not root.left:
            return (root.val, 1)
        left = self.helper(root.left)
        right = self.helper(root.right)
        # check depth
        if left[1] < right[1]:
            return (right[0], right[1] + 1)
        else:
            return (left[0], left[1]+1)

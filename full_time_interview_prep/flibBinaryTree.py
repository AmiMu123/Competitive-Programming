# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack = [root]
        vo_index = 0
        swap = []
        while stack:
            l = len(stack)
            node = stack.pop()
            if voyage[vo_index] != node.val:
                return [-1]
            if node.left :
                if voyage[vo_index + 1] != node.left.val:
                    node.left, node.right = node.right,node.left
                    swap.append(node.val)
            vo_index += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return swap
        
        
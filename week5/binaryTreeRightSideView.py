from collections import deque


class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            last = -1
            for i in range(len(queue)):
                node = queue.popleft()
                last = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(last)
        return res

from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    # dfs
    # max_height = 0
    # if not root:
    #     return 0
    # if not root.left and not root.right:
    #     return 0
    # if root.left and not root.right:
    #     left = height(root.left)
    #     max_height = max(max_height,left)
    # if root.right and not root.left:
    #     right = height(root.right)
    #     max_height = max(max_height,right)
    # if root.right and root.left:
    #     left = height(root.left)
    #     right = height(root.right)
    #     max_height = max(left,right)
    # return max_height + 1

    # bfs
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()
        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])
    return level

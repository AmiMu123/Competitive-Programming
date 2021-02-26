""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):
    lower = float("-inf")
    upper = float("inf")
    return isValid(root, lower, upper)


def isValid(root, lower, upper):
    if(root != None):
        if(lower < root.data < upper):
            return (isValid(root.left, lower, root.data) and isValid(root.right, root.data, upper))
        else:
            return False
    return True

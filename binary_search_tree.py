class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self, node):
        if self.val > node.val:
            if self.left == None:
                self.left = node
            else:
                self.left.insert(node)
        elif self.val < node.val:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(node)
        else:
            pass

    def search(self, node):
      if self.val == node.val:
        return self
      if self.val < node.val:
        if self.right == None:
          return None
        else:
          return self.right.search(node)
      if self.val > node.val:
        if self.left == None:
          return None
        else:
          return self.left.search(node)


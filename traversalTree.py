# Traversal of binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def height(self):
        if not self:
            return 0
        return 1 + max(self.height(self.left), self.height(self.right))

# bfs / level
def bfs(root):
    traversal = []
    h = root.height(root)
    for i in range(1, h+1):
        traversal.append(root, i)
 
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        return(root.val)
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

# dfs / in-order (left, root, right)
def dfs(root):
    traversal = []
    if not root:
        return 
    traversal = [root]
    dfs(root.left)
    dfs(root.right)
    return traversal

# pre-order (root, left, right)

# post-order (left, right, root)

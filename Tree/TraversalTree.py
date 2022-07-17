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

# dfs / in-order (left, root, right) - put dot on bottom
def dfs(root):
    # if root is None,return
    if root is None:
        return
    # traverse left subtree
    dfs(root.left)
    # print the current node
    print(root.val, end=" ,")
    # traverse right subtree
    dfs(root.right)

# pre-order (root, left, right) - put the dot on the left 
def preorder(root):
    # if root is None,return
    if root is None:
        return
    # print the current node
    print(root.val, end=" ,")
    # traverse left subtree
    preorder(root.left)
    # traverse right subtree
    preorder(root.right)
    

# post-order (left, right, root) - put the dot on the right
def postorder(root):
    # if root is None,return
    if root is None:
        return
    # traverse left subtree
    postorder(root.left)
    # traverse right subtree
    postorder(root.right)
    # print the current node
    print(root.val, end=" ,")
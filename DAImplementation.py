# stack needed for breadth first search 
stack = []
stack.append(2)
stack.pop()

# queue needed for depth first search
queue = []
queue.append(2)
queue.pop(0)

# hashmap
dict = []
dict[0] = 1
dict.contains(0) 
# returns true
max(dict, key=dict.get)
# return 0 => to get the value, dict[max(dict, key=dict.get)]

# to create an array (inline loop)
lst = [0 for i in range(10)]

# tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def height(self):
        if not self:
            return 0
        return 1 + max(self.height(self.left), self.height(self.right))

tree = TreeNode(0, 1, 2)

# 2d array
array = [ [0]*3 for i in range(3)]
# SUPER TRAP: [[v]*n]*n

# binary search tree implementation
class binarySearchTreeNode:
    # constructor
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        # if value to be inserted is less than the node, recurse to the left
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = binarySearchTreeNode(val)
            return

        # if value to be inserted is less than the node, recurse to the right
        if self.right:
            self.right.insert(val)
            return
        self.right = binarySearchTreeNode(val)

    def minValueNode(self):
        if self is None:
            return None
        elif self.left is None:
            return self
        else: 
            return self.left.minValueNode()

    def delete(self, key):
        if self is None:
            return self
        if key < self.key:
            self.left.delete(key)

        elif key > self.key:
            self.right.delete(key)
        
        # current node is to be delted
        else:
            # no predecessor
            if self.left is None:
                temp = self.right
                self = None
                return temp

            # no successor
            elif self.right is None:
                temp = self.left
                self = None
                return temp
 
            # node with two children, get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(self.right)
            self.key = temp.key
            
            # delete the inorder successor
            self.right.deleteNode(self.right, temp.key)
            
            return self

    def search(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.search(val)

        if self.right == None:
            return False
        return self.right.exists(val)

#Challenge: Find the most common N words in a file.

#BST sorting
class node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.left) + "<-" + str(self.value) + "->" + str(self.right)
    def getleft(self):
        return self.left.value
    def getright(self):
        return self.right.value
    def isleaf(self):
        return self.left is None and self.right is None

#inserts into a BST with recursion

def insert(BST, val):
    if BST.isleaf():
        if val <= BST.val:
            BST.left = node(val)
        else:
            BST.right = node(val)
    else:
        if val <= BST.val:
            if BST.left == None:
                BST.left = node(val)
            else:
                insert(BST.left, val)
        else:
            if BST.right == None:
                BST.right = node(val)
            else:
                insert(BST.right, val)

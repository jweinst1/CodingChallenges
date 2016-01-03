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
        if val <= BST.value:
            BST.left = node(val)
        else:
            BST.right = node(val)
    else:
        if val <= BST.value:
            if BST.left == None:
                BST.left = node(val)
            else:
                insert(BST.left, val)
        else:
            if BST.right == None:
                BST.right = node(val)
            else:
                insert(BST.right, val)

#gets the highest int in the bst
def get_max(BST):
    if BST.right == None:
        return BST.val
    else:
        return get_max(BST.right)

#gets the lowest int in the bst
def get_min(BST):
    if BST.left == None:
        return BST.val
    else:
        return get_min(BST.left)


#makes a btree
def make_BST(lst):
    assert len(lst) > 1
    btree = node(lst.pop())
    for elem in lst:
        insert(btree, elem)
    return btree

class keynode:

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    def getleft(self):
        return self.left.value
    def getright(self):
        return self.right.value
    def getvalue(self):
        return self.value
    def setvalue(self, elem):
        self.value = elem
    def isleaf(self):
        return self.left is None and self.right is None

#searches the tree based on the value
def search_KVtree(BST, value):
    if BST.isleaf() and BST.value is not value:
        return False
    elif BST.value == value:
       return BST.key
    elif value < BST.value:
       return search_KVtree(BST.left, value)
    else:
       return search_KVtree(BST.right, value)




def N_mostcommon_words(fname, N):
    with open(fname, 'r').read() as wordstring:
        wordstring = wordstring.split(" ")
        word_dict = {}
        for elem in wordstring:
            if elem in word_dict.keys():
                word_dict[elem] += 1
            else:
                word_dict[elem] = 1

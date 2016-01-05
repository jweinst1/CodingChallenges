#file for implementing square graphs

class squarenode:
# a four directional graph node
    def __init__(self, val, up=None, down=None, left=None, right=None):
        self.val = val
        self.up = up
        self.down = down
        self.left = left
        self.right = right
    def attachup(self, val):
        self.up = squarenode(val, None, self)
    def attachdown(self, val):
        self.down = squarenode(val, self)
    def attachleft(self, val):
        self.left = squarenode(val, None, None, None, self)
    def attachright(self, val):
        self.right = squarenode(val, None, None, self)



class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def build_line(n):
    line = squarenode(0)
    current = line
    i = 1
    while i < n:
        current.attachright(i)
        current = current.right
        i += 1
    return line
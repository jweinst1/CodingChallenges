#Challenge: Implement a binary tree of stacks
#all of the nodes are stacks

class stack:

    def __init__(self):
        self.container = []
    def __repr__(self):
        return str(self.container)
    def push(self, elem):
        self.container.append(elem)
    def pull(self):
        return self.container.pop()
    def peek(self):
        return self.container[len(self.container)-1]
    def isempty(self):
        return self.container is []


class stacknode:

    def __init__(self, value=stack(), left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.left) + "<-" + str(self.value) + "->" + str(self.right)
    def push(self, elem):
        self.value.push(elem)
    def pull(self):
        return self.value.pull()
    def peek(self):
        return self.value.peek()
    def isleaf(self):
        return self.left is None and self.right is None

#creates a stack tree recursively
def create_stack_tree(n):
    if n == 0:
        return None
    else:
        return stacknode(stack(), create_stack_tree(n-1), create_stack_tree(n-1))


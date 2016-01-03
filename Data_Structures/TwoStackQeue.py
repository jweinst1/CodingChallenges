#Challenge: Implement a queue with two stacks.

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

class twostackqueue:

    def __init__(self):
        self.instack = stack()
        self.outstack = stack()
    def __repr__(self):
        return str(self.instack) + '<->' + str(self.outstack)
    def enqueue(self, elem):
        self.instack.push(elem)
    def dequeue(self):
        if self.outstack.isempty():
            while not self.instack.isempty():
                self.outstack.push(self.instack.pull())
                return self.outstack.pull()
        else:
            return self.outstack.pull()

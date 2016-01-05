#challenge: Write a linked list that has both a last end and front end, that can be extended at both sides.

class link:

    def __init__(self, first, next=None):
        self.first = first
        self.next = next
    def __repr__(self):
        return str(self.first) + "->" + str(self.next)
    def hasnext(self):
        return self.next is not None
    def insert(self, val):
        self.next = link(val, self.next)


class two_tail_linkedlist:

    def __init__(self, front, back):
        self.front = link(front)
        self.front.insert(back)
        self.back = self.front.next
    def __repr__(self):
        return str(self.front)
    def addfront(self, val):
        self.front = link(val, self.front)
    def addback(self, val):
        self.back.insert(val)


#challenge: a linked list that has each node embedded in a dictionary

class linkedmap:

    def __init__(self, front, name):
        self.front = link(front)
        self.map = {}
        self.map[name] = self.front
        self.frontnum = 0
    def extendfront(self, val, name):
        self.front = link(val, self.front)
        self.map[name] = self.front
    def getmap(self):
        return self.map


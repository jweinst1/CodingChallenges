#CHallenge: Write a linked list imbedded in a map, where each node is indexed.
#This linked list will have O(1) insertions

class lnode:

    def __init__(self, first, rest=None):
        self.first = first
        self.rest = rest
    def __repr__(self):
        return str(self.first) + "->" + str(self.rest)
    def istail(self):
        return self.rest is None
    def attach(self, node):
        current = self.rest
        while current.rest != None:
            current = current.rest
        current.rest = node


class mappedLL:

    def __init__(self, val):
        self.map = []
        self.map.append(lnode(val))
        self.list = self.map[len(self.map)-1]
    def __repr__(self):
        return str(self.list)
    #every new node is also embedded in the map
    def add(self, val):
        self.map.append(lnode(val))
        self.list.attach(self.map[len(self.map)-1])




#Challenge: construct a list with it's sum already computed, and changes as it's set.


class sumlst:
    #has it's sum preset for faster retrieval
    def __init__(self, *args):
        self.lst = [elem for elem in args]
        self.sum = sum(self.lst)
    def __repr__(self):
        return str(self.lst)
    def sum(self):
        return self.sum
    def addnum(self, num):
        self.lst.append(num)
        self.reset_sum()
    def remove_num(self, num):
        self.lst.remove(num)
        self.reset_sum()
    def reset_sum(self):
        self.sum = sum(self.lst)
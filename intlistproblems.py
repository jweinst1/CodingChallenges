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



#Challenge: Return the number of even and odd numbers in a dictionary of a list in linear time.

def evenandodds(lst):
    nums = {'odd':0, 'even':0}
    for elem in lst:
        if elem % 2 ==0:
            nums['even'] += 1
        else:
            nums['odd'] += 1
    return nums

#Challenge: define a comprehension that get all elements that are even and odd in a dictionary

def evenplusodds(lst):
    nums = {'odd':[], 'even':[]}
    for elem in lst:
        if elem % 2 ==0:
            nums['even'].append(elem)
        else:
            nums['odd'].append(elem)
    return nums

#implement an array that has a fixed size, and can be extended by concatenating other arrays.
#it must also remove elements and copy them, without using builtin methods

class array:

    def __init__(self, size):
        self.size = size
        self.lst = [None for i in range(self.size)]
    def __setitem__(self, key, value):
        try:
            self.lst[key] = value
        except IndexError:
            return "key value is too high"
    def __getitem__(self, item):
        try:
            return self.lst[item]
        except IndexError:
            return "key value out of range"
    def copy(self):
        newarr = array(self.size)
        for i in range(self.size):
            newarr[i] = self.lst[i]
        return newarr
    #copies itself into a new array
    def copyinto(self, arr, start):
        for i in range(start, self.size):
            arr[i] = self.lst[i]
    #checks if any empty slots in the array
    def isfull(self):
        return None in self.lst
    def __iadd__(self, other):
        newarr = array(self.size+other.size)
        self.copyinto(newarr, 0)
        other.copyinto(newarr, other.size)
        return newarr

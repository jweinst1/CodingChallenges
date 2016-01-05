"""You have a sequence of all positive integer numbers from A to B. You changed each number x in that sequence to its digital root dr(x). Find the numbers that appear the most in the resulting sequence. Return them in the ascending order.

Example

digitalRoot("5", "9") = [5,6,7,8,9] since each of the resulting numbers appears exactly once even after you calculate the digital roots.

digitalRoot("12", "22") = [3,4] since 3 and 4 appear twice after you calculate the digital roots.

[input] string A

the lower bound as a string since it can be rather large < 10^15
[input] string B

the upper bound as a string since it can be rather large <10^15
[output] array.integer

the most common number in the final sequence"""



def digitalRoot(A, B):
    def dr(n):
        if len(str(n)) == 1:
            return n
        else:
            return dr(sum([int(elem) for elem in list(str(n))]))
    a = int(A)
    b = int(b)
    numlst = list(range(a, b+1))
    diglst = [dr(elem) for elem in numlst]
    countdict = {}
    for elem in diglst:
        if elem in countdict:
            countdict[elem] += 1
        else:
            countdict[elem] = 1
    return [elem for elem in countdict if countdict[elem] == max(countdict.values())]
#Challenge: Add two strings, which represent binary numbers together

def addbi(b1, b2):
    i = len(max(b1, b2)) -1
    newstr = ""
    carrystr = ""
    while i > 0:
        if b1[i] == "0" and b2[i] == "0":
            newstr = "0" + newstr
            i += 1
        elif b1[i] != b2[i]:
            newstr = "1" + newstr
            i+=1
        elif b1[i] =="1" and b2[i] == "1":
            carrystr += "1"
            newstr = "0" + newstr
            i+=1
    return newstr
import sys
import time

def bruteForce(pzl,dicthex):
    if isInvalid(pzl,dicthex) == True:
        return ""
    if isSolved(pzl) == True:
        print("Puzzle Solved!")
        print(pzl)
        return pzl
    x = pzl.find(".")
    for y in range(6):
        subPzl = pzl[:x]+str(y)+pzl[x+1:]
        bF = bruteForce(subPzl,dicthex)
        if bF != "":
            return pzl
    return ""

def isInvalid(pzl,dict):
    for values in dict.values():
        temp = []
        for x in range(len(values)):
            if pzl[values[x]:values[x]+1] != ".":
                temp.append(pzl[values[x]:values[x]+1])
        if len(temp) != len(set(temp)):
            return True
    list1 = [0,0,0,0,0,0]
    for z in range(24):
        if pzl[z:z+1] != ".":
            list1[int(pzl[z:z+1])] = list1[int(pzl[z:z+1])]+1
    for r in range(len(list1)):
        if list1[r]> 4:
            return True
    return False
def isSolved(pzl):
    if pzl.find(".") != -1:
        return False
    return True

hex = "........................"
dicthex = {0:(0,1,2,6,7,8),1:(2,3,4,8,9,10),2:(9,10,11,16,17,18),3:(15,16,17,21,22,23),4:(13,14,15,19,20,21),5:(5,6,7,12,13,14),6:(7,8,9,14,15,16)}
print(bruteForce(hex,dicthex))
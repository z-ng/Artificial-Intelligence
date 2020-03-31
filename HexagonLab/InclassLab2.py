import sys
import time
def bruteForce(pzl,dict,count):
    if isInvalid(pzl,dict) == True:
        return ""
    if isSolved(pzl) == True:
        print("Solution is",pzl)
        exit(0)
        return pzl
    index = pzl.find(".")
    for y in range(count):
        subPzl = pzl[:index]+str(y)+pzl[index+1:]
        bF = bruteForce(subPzl,dict,count)
        if bF != "":
            return pzl
    return ""

def isInvalid(pzl,dict):
    for key in dict.keys():
        atindex = pzl[key:key + 1]
        for x in range(0,3):
            if atindex != "." and atindex == pzl[dict[key][x]:dict[key][x]+1]:
                return True
    return False

def isSolved(pzl):
    if pzl.find(".") == -1:
        return True
    return False

hex = "...................."
count = 4
dict = {0:(1,4,6),1:(0,2,8),2:(1,3,10),3:(2,4,12),4:(0,3,14),5:(6,14,15),6:(0,5,7),7:(6,8,16),8:(1,7,9),9:(8,10,17),10:(2,9,11),11:(10,12,18),12:(3,11,13),13:(\
    12,14,19),14:(4,5,13),15:(5,16,19),16:(7,15,17),17:(9,16,18),18:(11,17,19),19:(13,15,18)}
temp = bruteForce(hex,dict,count)
print("No solution")
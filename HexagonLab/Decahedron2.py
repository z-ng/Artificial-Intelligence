import time
import sys

def bruteForce(pzl,dicthex,count,num):
    if isInvalid(pzl,dicthex) == True:
        return ""
    if isSolved(pzl) == True:
        tempdict = {}
        for f in range(count+1):
            tempdict[f] = []
        for h in range(len(pzl)):
            tempdict[int(pzl[h:h+1])].append(h)
        for keys, values in tempdict.items():
            if len(values) >= num:
                templist = []
                for g in range(num):
                    templist.append(values[g])
                print(templist,"are",num,"sides that do not touch one another")
                exit(0)
        return pzl
    index = pzl.find(".")
    for y in range(count):
        subPzl = pzl[:index]+str(y)+pzl[index+1:]
        bF = bruteForce(subPzl,dicthex,count,num)
        if bF != "":
            return pzl
    return ""

def isInvalid(pzl,dicthex):
    for key in dicthex.keys():
        temp = []
        for x in range(0,5):
            atindex = pzl[key:key+1]
            if atindex != "." and atindex == pzl[dicthex[key][x]:dicthex[key][x]+1]:
                return True
    return False

def isSolved(pzl):
    if pzl.find(".") == -1:
        return True
    return False

hex = "............"
num = int(''.join(sys.argv[1]))
count = 4
dicthex = {0:(1,2,3,4,5),1:(0,5,2,9,8),2:(0,1,3,7,8),3:(0,2,4,7,11),4:(0,3,5,11,10),5:(0,1,4,9,10),6:(7,8,9,10,11),7:(2,3,6,8,11),8:(1,2,6,7,9),9:(1,5,6,8,10),\
           10:(4,5,6,9,11),11:(3,4,6,7,10)}
temp = bruteForce(hex,dicthex,count,num)
print("No solution")
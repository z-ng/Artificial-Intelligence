import time

def bruteForce(pzl,dict,count,index):
    if isInvalid(pzl,dict,index) == True:
        return ""
    if isSolved(pzl) == True:
        return pzl
    spot = pzl.find(".")
    for y in range(1,10):
        subPzl = pzl[:spot]+str(y)+pzl[spot+1:]
        bF = bruteForce(subPzl,dict,count,spot)
        if bF != "":
            return bF
    return ""
def buildLookup(row,col):
    dict = {}
    for x in range(81):
        s = set()
        start = x-(x%9)
        for r in range(start,start+9):
            if r != x:
                s.add(r)
        for c in range(x%9,81,9):
            if c != x:
                s.add(c)
        count = 0
        corner = x
        while corner%3 != 0:
            corner = corner-1
        cornercopy = 0+corner
        while cornercopy >= 0:
            cornercopy = cornercopy-9
            count+=1
        corner = corner-(9*((count-1)%3))
        for h in range(0,3):
            for y in range(0,3):
                t = corner+(9*y)+(h)
                if t not in s and t != x:
                    s.add(t)
        dict[x] = s
    return dict

def isInvalid(pzl,dict,index):
    neighbors = dict.get(index)
    x = 0
    temp1 = pzl[index]
    for element in neighbors:
        temp2 = pzl[element]
        if temp2 == temp1 and temp1 != ".":
            return True
    return False

def isSolved(pzl):
    if pzl.find(".") == -1:
        return True
    return False
start = time.time()
row = 9
col = 9
dict = buildLookup(row,col)
count = 9
tup = ()
with open("9x9.txt","r") as f:
    tup = f.read().splitlines()
for x in range(51):
    print(str(x) + ". " + bruteForce(tup[x],dict,count,0))
print("Time taken",time.time()-start)
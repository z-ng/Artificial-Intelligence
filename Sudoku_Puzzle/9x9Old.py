import time

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




def bruteForce(pzl,dict,count,index,possibilities):
    if isSolved(pzl) == True:
        return pzl
    spot = findNext(pzl,possibilities)
    for y in range(1,10):
        if y not in possibilities[spot]:
            subPzl = pzl[:spot]+str(y)+pzl[spot+1:]
            s = []
            for value in possibilities:
                s.append(value.copy())
            s[spot].add(y)
            for i in dict[spot]: #adds to all spots neighbors
                if y not in s[i]:
                    s[i].add(y)
            bF = bruteForce(subPzl,dict,count,spot,s)
            for value in s:
                s.remove(value.copy())
            if bF != "":
                return bF
    return ""

def findNext(pzl,possibilities):
    largestSet = 0
    for x in range(0,len(possibilities),1):
        if pzl[x] == "." and len(possibilities[x]) > largestSet:
            largestSet = len(possibilities[x])
            index = x
    return index

def isSolved(pzl):
    if pzl.find(".") == -1:
        return True
    return False

def buildPossible(pzl,dict):
    possibilities = []
    for y in range(len(pzl)):
        possibilities.append(set())
    for x in range(len(pzl)):
        if pzl[x] != ".":
            for value in dict.get(x):
                if pzl[x] not in possibilities[value]:
                    possibilities[value].add(int(pzl[x]))
    return possibilities

start = time.time()
row = 9
col = 9
dict = buildLookup(row,col)
count = 9
tup = ()
with open("9x9all.txt","r") as f:
    tup = f.read().splitlines()
for x in range(len(tup)):
    possibilities = buildPossible(tup[x],dict)
    print(x,bruteForce(tup[x],dict,count,0,possibilities))
print("Time taken",time.time()-start)
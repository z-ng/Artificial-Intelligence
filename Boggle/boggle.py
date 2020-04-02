import re
import math
import sys
import time

def buildLookup(rowLen):
    dct = {}
    largestSpace = rowLen*rowLen
    for x in range(largestSpace):
        tmp = []
        if x-rowLen >= 0:
            tmp.append(x-rowLen)
        if x+rowLen < largestSpace:
            tmp.append(x+rowLen)
        if (x-1)//rowLen == x//rowLen:
            tmp.append(x-1)
        if (x+1)//rowLen == x//rowLen:
            tmp.append(x+1)
        if x-rowLen-1 >= 0 and (x//rowLen)-((x-rowLen-1)//rowLen) == 1:
            tmp.append(x-rowLen-1)
        if x-rowLen+1 >= 0 and (x//rowLen)-((x-rowLen+1)//rowLen) == 1:
            tmp.append(x-rowLen+1)
        if x+rowLen+1 < largestSpace and (x//rowLen)-((x+rowLen+1)//rowLen) == -1:
            tmp.append(x+rowLen+1)
        if x+rowLen-1 < largestSpace and (x//rowLen)-((x+rowLen-1)//rowLen) == -1:
            tmp.append(x+rowLen-1)
        dct[x] = tmp
    return dct

def recur(possibleWords,traveledPositions,board,word,position,lookUp):
    regex = r"^" + re.escape(word) + r"[a-z]*$"
    foundWords = []
    if word in possibleWords:
        foundWords.append(word)
    tmpArr = []
    for x in possibleWords:
        if re.search(regex, x):
            tmpArr.append(x)
    if len(tmpArr) == 0:
        return foundWords
    else:
        for x in lookUp[position]:
            if x not in traveledPositions and board[x] != "_":
                traveledPositions.append(x)
                foundWords = foundWords + recur(tmpArr,traveledPositions,board,word+board[x],x,lookUp)
                traveledPositions.remove(x)
        return foundWords



# fl = 'wordss.txt'
# readDct = open("dict.txt",'w').write("\n".join(open(fl,"r").read().splitlines()))
dct = open("dict.txt",'r').read().splitlines()

boggleBoard = str(sys.argv[1]).lower()

tmpBoggle = []
count = 0
while count < len(boggleBoard):
    if boggleBoard[count] not in ['1','2','3','4','5','6','7','8','9','0']:
        tmpBoggle.append(boggleBoard[count])
        count+=1
    else:
        numIndex = count
        while boggleBoard[numIndex] in ['1','2','3','4','5','6','7','8','9','0']:
            numIndex+=1
        tmpCount = count+1
        numIter = int(''.join(boggleBoard[count:numIndex]))
        count = count+numIter+1
        tmpStr = ""
        while tmpCount < count:
            tmpStr = tmpStr + boggleBoard[tmpCount]
            tmpCount+=1
        tmpBoggle.append(tmpStr)
boggleBoard = tmpBoggle.copy()
print(boggleBoard)

boardLen = int(math.sqrt(len(boggleBoard)))
print("This is a",boardLen,'x',boardLen,"boggle board")
lookUp = buildLookup(boardLen)

print("Original length",len(dct))
dctCopy = []
for x in dct:
    dctCopy.append(x.lower())
dct = dctCopy.copy()
dctCopy = []
if boardLen == 4:
    for x in dct:
        m = re.search(r"^\w*[aeiou]\w*$", x)
        if m:
            dctCopy.append(x)
elif boardLen > 4:
    for x in dct:
        m = re.search(r"^\w{1,99}[aeiou]\w{1,99}$|^\w{2,99}[aeiou]$|^[aeiou]\w{2,99}$", x)
        if m:
            dctCopy.append(x)
else:
    for x in dct:
        m = re.search(r"^\w*[aeiou]\w*$", x)
        if m:
            dctCopy.append(x)
    print("HELLO")
print("Length after trim",len(dctCopy))

start = time.time()
allWords = []
index = 0
for x in boggleBoard:
    tmpArr = []
    regex = r"^" + re.escape(x) + r"[a-z]*$"
    for y in dctCopy:
        if re.search(regex, y):
            tmpArr.append(y)
    print(lookUp[index])
    for h in lookUp[index]:
        print(h)
        allWords = allWords + recur(tmpArr,[index,h],boggleBoard,x+boggleBoard[h],h,lookUp)
    index+=1
allWords = set(allWords)
print("There are",len(allWords),"words.  They are listed below:")
print(allWords)
print(time.time()-start)
# def recur(possibleWords,traveledPositions,board,word,position,lookUp):
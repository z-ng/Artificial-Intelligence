import sys
import time
import random

def swap(index, orig, str):
    chars = list(str)
    chars[index], chars[orig] = chars[orig], chars[index]
    return ''.join(chars)
def findPositions(str):
    index = str.find("_")
    dict = {0:{1,3},1:{0,2,4},2:{1,5},3:{0,4,6},4:{1,3,5,7},5:{2,4,8},6:{3,7},7:{4,6,8},8:{5,7}}
    arr1 = []
    for x in dict[index]:
        arr1.append(swap(x,index,str))
    return arr1


#PART 7


start = time.time()
steps = 0
numsolve = 0
input = "12345678_"
for z in range(0, 100, 1):
    input = ''.join(random.sample(input,len(input)))
    parseMe = findPositions(input)
    alreadySeen = {input:input}
    final = "12345678_"
    popcount = 0
    if input != final:
        for h in range(0,len(parseMe),1):
            alreadySeen[parseMe[h]] = input
        while final not in alreadySeen and len(parseMe) != popcount:
            str = ''.join(parseMe[popcount])
            arrcount = 0
            array = findPositions(str)
            for x in range(0,len(array),1):
                temp = ''.join(array[arrcount])
                if temp not in alreadySeen:
                    parseMe.append(temp)
                    alreadySeen[temp] = str
                arrcount = arrcount+1
            popcount = popcount+1
        str = "12345678_"
        find = ""
        arr = [str]
        if len(parseMe) != popcount:
            while str != input:
                for key, value in alreadySeen.items():
                    if key == str:
                        find = value[:]
                str = find[:]
                arr.append(str)
                steps = steps+1
            numsolve = numsolve+1
    else:
        numsolve = numsolve+1
if steps != 0:
    steps = steps/numsolve
print("Average number of steps", steps)
print("Average time",":",(time.time() - start) / 1000)
print("\n\n")



# PART 8


input = "12345678_"
parseMe = findPositions(input)
alreadySeen = {input}
tempset = set()
dict = {0:"1234567_8",1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0}
states = set()

for h in range(0,len(parseMe),1):
    alreadySeen.add(parseMe[h])
states.add("1234567_8")
states.add("1234_6758")
states.add("123456_78")
states.add("12345678_")
for r in range(1,31,1):
    while len(parseMe) != 0:
        str = ''.join(parseMe.pop())
        array = findPositions(str)
        for x in range(0,len(array),1):
            word = ''.join(array[x])
            if word not in alreadySeen:
                tempset.add(''.join(array[x]))
                alreadySeen.add(''.join(array[x]))
                if dict.get(r) == 0:
                    bool = False
                    temparr = findPositions(word)
                    for h in range(0, len(temparr),1):
                        if temparr[h] in states:
                            bool = True
                    if bool == False:
                        for w in range(0, len(temparr),1):
                            states.add(temparr[h])
                            dict[r] = ''.join(array[x])
    parseMe = tempset.copy()
    tempset = set()
for key, value in dict.items():
    if key == 0:
        print(key+1,"step away goal",":",value)
    else:
        print(key+1,"steps away from goal", ":", value)
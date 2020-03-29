import sys
import time

def swap(index, orig, str):
    chars = list(str)
    chars[index], chars[orig] = chars[orig], chars[index]
    return ''.join(chars)
def findPositions(str):
    index = str.find("_")
    dict = {0:{1,3},1:{0,2,4},2:{1,5},3:{0,4,6},4:{1,3,5,7},5:{2,4,8},6:{3,7},7:{4,6,8},8:{5,7}}
    arr = []
    for x in dict[index]:
        arr.append(swap(x,index,str))
    return arr

start = time.time()


input = "12345678_"
parseMe = findPositions(input)
alreadySeen = {input}
tempset = set()
count = 0
dict = {0:1,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0}

for h in range(0,len(parseMe),1):
    alreadySeen.add(parseMe[h])
for r in range(1,31,1):
    while len(parseMe) != 0:
        str = ''.join(parseMe.pop())
        array = findPositions(str)
        for x in range(0,len(array),1):
            if ''.join(array[x]) not in alreadySeen:
                tempset.add(''.join(array[x]))
                alreadySeen.add(''.join(array[x]))
                count = count + 1
    dict[r] = count
    count = 0
    parseMe = tempset.copy()
    tempset = set()
for x in range(0,31,1):
    print(x+1, ":",dict.get(x))

print(time.time()-start)


print("Longest distance = 31")
input = "8672543_1"
parseMe = findPositions(input)
alreadySeen = {input:input}
final = "12345678_"
if input == final:
    print("123\n456\n78_")
    print("\nIt took 0 steps")
    sys.exit(1)
for h in range(0,len(parseMe),1):
    alreadySeen[parseMe[h]] = input
while final not in alreadySeen:
    if len(parseMe) == 0:
        print("No solution")
        sys.exit(1)
    str = ''.join(parseMe.pop(0))
    array = findPositions(str)
    for x in range(0,len(array),1):
        if ''.join(array[x]) not in alreadySeen:
            parseMe.append(''.join(array[x]))
            alreadySeen[''.join(array[x])] = str
str = "12345678_"
find = ""
arr = [str]
while str != input:
    for key, value in alreadySeen.items():
        if key == str:
            find = value[:]
    str = find[:]
    arr.append(str)
print("\n")
count = 0
for x in range(len(arr)-1,-1,-1):
    print(arr[x][0:3])
    print(arr[x][3:6])
    print(arr[x][6:])
    print("\n")
    count = count+1
print(count-1)
print("Puzzle completed!")
print("Time taken:", time.time()-start)



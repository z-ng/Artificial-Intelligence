import sys
import time

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

start = time.time()
input = ''.join(sys.argv[1])
print('\n'+input)
#Example Case "241753_86"
parseMe = findPositions(input)
alreadySeen = {input:input}
final = "12345678_"
popcount = 0
if input == final:
    print("123\n456\n78_")
    print("\nIt took 0 steps")
    sys.exit(1)
for h in range(0,len(parseMe),1):
    alreadySeen[parseMe[h]] = input
while final not in alreadySeen:
    if len(parseMe) == popcount:
        print("No solution")
        print(time.time()-start)
        sys.exit(1)
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
print(time.time()-start)
print("Puzzle completed!")
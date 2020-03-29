import sys
import time
import heapq


def swap(index, orig, str):
    chars = list(str)
    chars[index], chars[orig] = chars[orig], chars[index]
    return ''.join(chars)
def findPositions(str):
    index = str.find("_")
    dict = {0:{1,4},1:{0,2,5},2:{1,3,6},3:{2,7},4:{0,5,8},5:{1,4,6,9},6:{2,5,7,10},7:{3,6,11},8:{4,9,12},9:{5,8,10,13},10:{6,9,11,14},11:{7,10,15},12:{8,13},13:{9,12,14},14:{10,13,15},15:{11,14}}
    arr1 = []
    for x in dict[index]:
        arr1.append(swap(x,index,str))
    return arr1
def findDistance(str, final):
    distance = 0
    for x in range(0,len(str),1):
        if str[x:x+1] != "_":
            index = final.find(str[x:x+1])
            distance = distance + (abs((index%4)-(x%4))+abs((index//4)-(x//4)))
    return distance


start = time.time()
states = 0
improved = 0
input = ''.join(sys.argv[1])
final = "ABCDEFGHIJKLMNO_"
find = {}   #used for ease of access
parseMe = []
temp = findPositions(input)
for x in range(0,len(temp),1):
    tup = ((findDistance(temp[x],final)),temp[x],0)
    heapq.heappush(parseMe,tup)
    find[temp[x]] = tup
path = {input:input}    #used to find path back
popped = set()      #find popped elements
popcount = 0
if input == final:
    print("ABCD\nEFGH\nIJKL\nMNO_")
    print("\nIt took 0 steps")
    sys.exit(1)
templist = []
while len(parseMe) != 0 == False:
    temp = heapq.heappop(parseMe)
    templist.append(temp)
    path[temp[1]] = input
for g in range(0,len(templist),1):
    heapq.heappush(parseMe,templist[g])
    find[templist[g][1]] = templist[g]
while final not in path.keys():
    if len(parseMe) == 0:   #checks if no solution
        print("No solution")
        print(time.time()-start)
        sys.exit(1)
    pop = heapq.heappop(parseMe)      #removes top from heapq
    find.pop(pop[1])
    states = states+1       #counts states removed
    array = findPositions(''.join(pop[1]))      #find neighbors
    steps = pop[2]+1    #counts the current steps
    for x in range(0,len(array),1):     #runs through neighbors
        temp = ''.join(array[x])    #1 neighbor
        if temp not in popped and temp not in find.keys():  #checks if its been popped and its not in parseMe
            tup = (findDistance(temp, final) + steps, temp, steps)  #tup of distance,state,steps
            heapq.heappush(parseMe, tup)
            path[temp] = pop[1]
            find[temp] = tup
        elif temp not in popped and temp in find.keys():    #if its not in popped but in parseMe
            if find.get(temp)[0] > findDistance(temp,final) + steps:  #if the current state is smaller than the one in find
                tup = (findDistance(temp, final) + steps, temp, steps)
                parseMe.remove(find.get(temp)) #remove from parseMe
                heapq.heappush(parseMe,tup) #re-adds it
                path[temp] = pop[1]
                improved = improved + 1
                find[temp] = tup    #change find value
    popped.add(pop[1])  #added the removed value from popped
str = "ABCDEFGHIJKLMNO_"
find = ""
arr = [str]
while str != input:
    for key, value in path.items():
        if key == str:
            find = value[:]
    str = find[:]
    arr.append(str)
print("\n")
count = 0
for x in range(len(arr)-1,-1,-1):
    print(arr[x][0:4])
    print(arr[x][4:8])
    print(arr[x][8:12])
    print(arr[x][12:])
    print("\n")
    count = count+1
    time.sleep(0.2)

print("Takes:",int(count-1),"steps to solve")
print("Takes",time.time()-start, "seconds to run")
print("Number of states removed",states)
print("Number of improvements made",improved)
print("Size of closed set",len(popped))
print("Puzzle completed!")
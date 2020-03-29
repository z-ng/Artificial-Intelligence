import time
import tkinter
from tkinter import *
from math import sin, cos, sqrt, atan2, radians
import heapq

def findDistance(x1,y1,x2,y2):
    radius = 3958.7 # radius of earth miles

    lat1 = radians(x1)
    lon1 = radians(y1)
    lat2 = radians(x2)
    lon2 = radians(y2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius * c
    return distance

def circle(canvas,x,y, r,color):
   id = canvas.create_oval(x-r,y-r,x+r,y+r,fill=color,outline='')
   return id

#MAIN

input = "cursor"
start = time.time()
city = {}
nodes = {}
edges = {}
added = []

with open("cities.txt","r") as ins:
    for lines in ins:
        city[lines[0:1]] = lines
with open("edges.txt","r") as ins:
    for lines in ins:
        temp = lines.split()
        if temp[0] not in added:
            edges[temp[0]] = []
            added.append(temp[0])
        if temp[1] not in added:
            edges[temp[1]] = []
            added.append(temp[1])
        edges.get(temp[0]).append(temp[1])
        edges.get(temp[1]).append(temp[0])
with open("nodes.txt","r") as ins:
    for lines in ins:
        temp = lines.split()
        nodes[temp[0]] = (temp[1],temp[2])

root = tkinter.Tk()
myframe = Frame(root)
h = 500
w = 800
mycanvas = Canvas(root,width=w,height=h)
mycanvas.pack()

totald = 0 #1398.4

#for astar
visited = set()
input = sys.argv[1]
final = sys.argv[2]
completed = False

if input == final:
    print("You are at your destination!")
    print("Distance traveled is 0")
    completed = True
    exit()

find = {}  # used for ease of access
parseMe = []
temp = edges.get(input)
for x in range(0, len(temp), 1):
    neighbor = temp.pop()
    heuristic = findDistance(float(nodes.get(neighbor)[0]),float(nodes.get(neighbor)[1]), float(nodes.get(final)[0]),float(nodes.get(final)[1]))
    dstart = findDistance(float(nodes.get(neighbor)[0]),float(nodes.get(neighbor)[1]),float(nodes.get(input)[0]),float(nodes.get(input)[1]))
    tup = (heuristic+dstart,neighbor,dstart)
    heapq.heappush(parseMe, tup)
    find[neighbor] = tup
path = {input: input}  # used to find path back
popped = set()  # find popped elements aka closed set
templist = []
while len(parseMe) != 0 == False:
    temp = heapq.heappop(parseMe)
    templist.append(temp)
    path[temp[1]] = input
for g in range(0, len(templist), 1):
    heapq.heappush(parseMe, templist[g])
    find[templist[g][1]] = templist[g]

while True:

    for key,value in edges.items():
        for x in range(0,len(value),1):
            temp = value[x]
            scale = 100
            vary = -4300
            varx = +2100
            circle(mycanvas,((float(nodes.get(temp)[1]))*scale)-varx, (h-(float(nodes.get(temp)[0]))*scale)-vary,4,"yellow")
            circle(mycanvas,((float(nodes.get(key)[1]))*scale)-varx, (h-(float(nodes.get(key)[0]))*scale)-vary,4,"yellow")
            mycanvas.create_line(((float(nodes.get(temp)[1]))*scale)-varx, (h-(float(nodes.get(temp)[0]))*scale)-vary, (float(nodes.get(key)[1])*scale)-varx, (h-(float(nodes.get(key)[0]))*scale)-vary)
            totald = totald + findDistance(float(nodes.get(temp)[0]),float(nodes.get(temp)[1]),float(nodes.get(key)[0]),float(nodes.get(key)[1]))

    if completed == False and final not in path.keys():
        if len(parseMe) == 0:  # checks if no solution
            print("No Path Found")
            print(time.time() - start)
            completed = True
        pop = heapq.heappop(parseMe)  # removes top from heapq
        find.pop(pop[1])
        array = list(edges.get(pop[1]))  # find neighbors
        dstart = pop[2]  # distance from start
        for x in range(0, len(array), 1):  # runs through neighbors
            temp = ''.join(array[x])  # 1 neighbor
            if temp not in popped and temp not in find.keys():  # checks if its been popped and its not in parseMe
                heuristic = findDistance(float(nodes.get(temp)[0]), float(nodes.get(neighbor)[1]),
                                         float(nodes.get(final)[0]), float(nodes.get(final)[1]))
                dnode = findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]), float(nodes.get(pop[1])[0]),
                                     float(nodes.get(pop[1])[1]))
                tup = (heuristic + dstart + dnode, temp, dstart + dnode)
                heapq.heappush(parseMe, tup)
                path[temp] = pop[1]
                find[temp] = tup
            elif temp not in popped and temp in find.keys():  # if its not in popped but in parseMe
                heuristic = findDistance(float(nodes.get(temp)[0]), float(nodes.get(neighbor)[1]),
                                         float(nodes.get(final)[0]), float(nodes.get(final)[1]))
                dnode = findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]), float(nodes.get(pop[1])[0]),
                                     float(nodes.get(pop[1])[1]))
                tup = (heuristic + dstart + dnode, temp, dstart + dnode)
                if find.get(temp)[0] > heuristic + dnode:  # if the current state is smaller than the one in find
                    # parseMe.remove(find.get(temp))  remove not needed, you can simply just add only effects memory
                    heapq.heappush(parseMe, tup)  # re-adds it
                    path[temp] = pop[1]
                    find[temp] = tup  # change find value
        popped.add(pop[1])  # added the removed value from popped
    if completed == False and final in path.keys():
        str = final
        arr = [str]
        while str != input:
            for key, value in path.items():
                if key == str:
                    find = value[:]
            str = find[:]
            arr.append(str)
        print("\n")
        print("Path From City", input, "to City", final, "\n")
        prev = input
        distance = 0
        for x in range(len(arr) - 1, -1, -1):
            cityd = findDistance(float(nodes.get(prev)[0]), float(nodes.get(prev)[1]), float(nodes.get(arr[x])[0]),float(nodes.get(arr[x])[1]))
            if arr[x] != input:
                print("Distance from", prev, "to", arr[x], "is", cityd)
            prev = arr[x]
            distance = cityd + distance
        print("\nTotal distance traveled from", input, "to", final, "is", distance, "miles")
        completed = True
    copyPop = popped.copy()
    copyParse = parseMe.copy()
    while len(copyPop) != 0:
        coord = copyPop.pop()
        circle(mycanvas, ((float(nodes.get(coord)[1])) * scale) - varx, (h - (float(nodes.get(coord)[0])) * scale) - vary,4, "blue")
    while len(copyParse) != 0:
        coord = copyParse.pop()[1]
        circle(mycanvas, ((float(nodes.get(coord)[1])) * scale) - varx, (h - (float(nodes.get(coord)[0])) * scale) - vary,4, "red")
    if completed == True:
        prev = input
        for x in range(len(arr) - 1, -1, -1):
            mycanvas.create_line(((float(nodes.get(prev)[1])) * scale) - varx, (h - (float(nodes.get(prev)[0])) * scale) - vary,\
            (float(nodes.get(arr[x])[1]) * scale) - varx, (h - (float(nodes.get(arr[x])[0])) * scale) - vary,fill="darkgreen")
            prev = arr[x]

    Tk.update_idletasks(root)
    Tk.update(root)
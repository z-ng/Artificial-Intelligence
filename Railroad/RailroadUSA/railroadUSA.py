import time
import tkinter
from tkinter import *
from math import sin, cos, sqrt, atan2, radians, pi, acos
import sys
import time
import heapq



def findDistance(y1,x1, y2,x2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   d = sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1)
   if d > 1:
       d = 1
   if d < -1:
       d = -1
   return acos( d ) * R

def circle(canvas,x,y, r,color):
   id = canvas.create_oval(x-r,y-r,x+r,y+r,fill=color,outline='')
   return id


input = "cursor"
start = time.time()
city = {}
nodes = {}
edges = {}
added = set()

with open("cities.txt","r") as ins:
    for lines in ins:
        temp = lines.split()
        city[' '.join(temp[1:])] = ''.join(temp[0:1])
with open("edges.txt","r") as ins:
    for lines in ins:
        temp = lines.split()
        if temp[0] not in added:
            edges[temp[0]] = set()
            added.add(temp[0])
        if temp[1] not in added:
            edges[temp[1]] = set()
            added.add(temp[1])
        edges.get(temp[0]).add(temp[1])
        edges.get(temp[1]).add(temp[0])
with open("nodes.txt","r") as ins:
    for lines in ins:
        temp = lines.split()
        nodes[temp[0]] = (temp[1],temp[2])


start = time.time()
root = tkinter.Tk()
myframe = Frame(root)
h = 720
w = 1280
mycanvas = Canvas(root,width=w,height=h)
mycanvas.pack()

totald = 0

visited = set()
input = sys.argv[1]
final = sys.argv[2]
print(input,final)
if input in city:
    input = city.get(input)
if final in city:
    final = city.get(final)
completed = False
if input == final:
    print("You are at your destination!")
    print("Distance traveled is 0")
    completed = True

find = {}
parseMe = []
temp = edges.get(input)
for x in range(0, len(temp), 1):
    neighbor = temp.pop()
    heuristic = findDistance(float(nodes.get(neighbor)[0]), float(nodes.get(neighbor)[1]),float(nodes.get(final)[0]), float(nodes.get(final)[1]))
    dnode = findDistance(float(nodes.get(neighbor)[0]), float(nodes.get(neighbor)[1]), float(nodes.get(input)[0]),float(nodes.get(input)[1]))
    tup = (heuristic + dnode, neighbor, dnode)
    heapq.heappush(parseMe, tup)
    find[neighbor] = tup
path = {input: input}  # used to find path back
popped = set()  # find popped elements aka closed set
templist = []
circles = {}
for key, value in edges.items():
    for x in range(0, len(value), 1):
        temp = list(value)[x]
        scale = 13
        vary = -100
        varx = -1900
        circles[temp] = circle(mycanvas, ((float(nodes.get(temp)[1])) * scale) - varx, (h - (float(nodes.get(temp)[0])) * scale) - vary,1, "pink")
        circles[key] = circle(mycanvas, ((float(nodes.get(key)[1])) * scale) - varx, (h - (float(nodes.get(key)[0])) * scale) - vary,1, "pink")
        mycanvas.create_line(((float(nodes.get(temp)[1])) * scale) - varx,(h - (float(nodes.get(temp)[0])) * scale) - vary,(float(nodes.get(key)[1]) * scale) - varx, (h - (float(nodes.get(key)[0])) * scale) - vary)
        totald = totald + findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]), float(nodes.get(key)[0]),float(nodes.get(key)[1]))
while len(parseMe) != 0 == False:
    temp = heapq.heappop(parseMe)
    templist.append(temp)
    path[temp[1]] = input
for g in range(0, len(templist), 1):
    heapq.heappush(parseMe, templist[g])
    find[templist[g][1]] = templist[g]

update = 0
Tk.update(root)
time.sleep(6)
while True:
    if completed == False and final not in path.keys():
        if len(parseMe) == 0:  # checks if no solution
            print("No Path Found")
            print(time.time() - start)
            completed = True
        pop = heapq.heappop(parseMe)  # removes top from heapq
        if pop[1] not in popped:
            find.pop(pop[1])
            array = list(edges.get(pop[1]))  # find neighbors
            dstart = pop[2]  # distance from start
            for x in range(0, len(array), 1):  # runs through neighbors
                temp = ''.join(array[x])  # 1 neighbor
                if temp not in popped and temp not in find.keys():  # checks if its been popped and its not in parseMe
                    heuristic = findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]),float(nodes.get(final)[0]), float(nodes.get(final)[1]))
                    dnode = findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]),float(nodes.get(pop[1])[0]), float(nodes.get(pop[1])[1]))
                    tup = (heuristic + dstart + dnode, temp, dstart + dnode)
                    heapq.heappush(parseMe, tup)
                    mycanvas.itemconfigure(circles[temp], fill = "blue")
                    path[temp] = pop[1]
                    find[temp] = tup
                elif temp not in popped and temp in find.keys():  # if its not in popped but in parseMe
                    heuristic = findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]),float(nodes.get(final)[0]), float(nodes.get(final)[1]))
                    dnode = findDistance(float(nodes.get(temp)[0]), float(nodes.get(temp)[1]),float(nodes.get(pop[1])[0]), float(nodes.get(pop[1])[1]))
                    tup = (heuristic + dstart + dnode, temp, dstart + dnode)
                    if find.get(temp)[0] > heuristic+dstart+dnode:  # if the current state is smaller than the one in find
                        heapq.heappush(parseMe, tup)  # re-adds it
                        path[temp] = pop[1]
                        find[temp] = tup  # change find value
            popped.add(pop[1])  # added the removed value from popped
            mycanvas.itemconfigure(circles[pop[1]], fill = "limegreen")
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
        mycanvas.itemconfigure(circles[input],fill="red")
        for x in range(len(arr) - 1, -1, -1):
            cityd = findDistance(float(nodes.get(prev)[0]), float(nodes.get(prev)[1]), float(nodes.get(arr[x])[0]),float(nodes.get(arr[x])[1]))
            if arr[x] != input:
                print("Distance from", prev, "to", arr[x], "is", cityd)
                mycanvas.itemconfigure(circles[arr[x]], fill="red")
            prev = arr[x]
            distance = cityd + distance
        mycanvas.itemconfigure(circles[final], fill="red")
        print("\nTotal distance traveled from", input, "to", final, "is", distance, "miles")
        print("Time to run:", time.time()-start,"seconds")
        completed = True
    if update == 1000:
        Tk.update(root)
        update = 0
    else:
        update+= 1
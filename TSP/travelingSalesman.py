import time
import tkinter
from tkinter import *
from math import sin, cos, sqrt, atan2, radians
import itertools

def findDistance(x1,y1,x2,y2):
    #radius = 3958.7 # radius of earth miles
    radius = 6371.0 #radius of earth kilomters
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

def findPathDistance(path):
    totalDistance = 0
    for x in range(len(path) - 1):
        totalDistance += findDistance(path[x][1], path[x][0], path[x + 1][1], path[x + 1][0])
    totalDistance+=findDistance(path[0][0],path[0][1],path[len(path)-1][0],path[len(path)-1][1])
    return totalDistance

def findSegmentDistance(path):
    totalDistance = 0
    for x in range(len(path) - 1):
        totalDistance += findDistance(path[x][1], path[x][0], path[x + 1][1], path[x + 1][0])
    return totalDistance

def greedyPath(path):
    tmpPath = path.copy()
    tmpPath.remove(path[0])
    newPath = [path[0]]
    count = 1
    while count != len(path):
        shortestDistance = 999999999999
        bestNode = tmpPath[0]
        for x in tmpPath:
            if findDistance(x[0],x[1],newPath[count-1][0],newPath[count-1][1]) < shortestDistance:
                bestNode = x
                shortestDistance = findDistance(x[0],x[1],newPath[count-1][0],newPath[count-1][1])
        newPath.append(bestNode)
        tmpPath.remove(bestNode)
        count+=1
    return newPath


def untangle(path): #iterative
    oldPath = []
    newPath = path
    pathTried = []
    dctOfDistances = {}
    while oldPath != newPath:
        oldPath = newPath.copy()
        for i in range(-1,len(path)-3):
            brokenOut = False
            firstNode = oldPath[i]
            secondNode = oldPath[i+1]
            for j in range(i+2,len(path)-1):
                if i ==-1 and j==len(path)-2:
                    continue
                thirdNode = oldPath[j]
                if j == len(oldPath) - 1:
                    fourthNode = oldPath[0]
                else:
                    fourthNode = oldPath[j+1]
                if firstNode != thirdNode and firstNode != fourthNode and secondNode != thirdNode and secondNode != fourthNode:
                    if (firstNode,secondNode) not in dctOfDistances or (secondNode,firstNode) not in dctOfDistances:
                        dctOfDistances[(firstNode,secondNode)] = findDistance(firstNode[0],firstNode[1],secondNode[0],secondNode[1])
                    if (thirdNode, fourthNode) not in dctOfDistances or (fourthNode, thirdNode) not in dctOfDistances:
                        dctOfDistances[(thirdNode,fourthNode)] = findDistance(thirdNode[0],thirdNode[1],fourthNode[0],fourthNode[1])
                    if (firstNode, thirdNode) not in dctOfDistances or (thirdNode,firstNode) not in dctOfDistances:
                        dctOfDistances[(firstNode,thirdNode)] = findDistance(firstNode[0],firstNode[1],thirdNode[0],thirdNode[1])
                    if (secondNode,fourthNode) not in dctOfDistances or (fourthNode,secondNode) not in dctOfDistances:
                        dctOfDistances[(secondNode,fourthNode)] = findDistance(secondNode[0],secondNode[1],fourthNode[0],fourthNode[1])
                    if dctOfDistances[(firstNode,secondNode)] + dctOfDistances[(thirdNode,fourthNode)] > dctOfDistances[(firstNode,thirdNode)] + dctOfDistances[(secondNode,fourthNode)]:
                        newPath = oldPath[0:i+1] + oldPath[i+1:oldPath.index(fourthNode)][::-1] + oldPath[oldPath.index(fourthNode):]
                        if newPath not in pathTried:
                            brokenOut = True
                            break
            if brokenOut == True:
                break
        print(findPathDistance(newPath))
        print("OLDPATH",oldPath)
        print("NEWPATH",newPath)
    return newPath

def permut(path):
    noImprovement = True
    bestPath = path
    while noImprovement == True:
        noImprovement = False
        n = 8
        for x in range(0,len(path)-n,1):
            curPathLength = findSegmentDistance(bestPath[x:x+n])
            curPathArr = bestPath[x:x+n]
            permutations = itertools.permutations(bestPath[x:x+n])
            for y in permutations:
                if y[0] == bestPath[x] and y[n-1] == bestPath[x+n-1]:
                    if findSegmentDistance(y) < curPathLength:
                        curPathLength = findSegmentDistance(y)
                        curPathArr = list(y)
                        noImprovement = True
            if bestPath[x:x+n] != curPathArr:
                returnOld = bestPath[x:x+n].copy()
                returnNew = curPathArr.copy()
            bestPath = bestPath[0:x] + curPathArr + bestPath[x+n:]
    return bestPath

def circle(canvas,x,y, r,color):
   id = canvas.create_oval(x-r,y-r,x+r,y+r,fill=color,outline='')
   return id

def findTruePath(originalNodePath,newArr):
    totalD = 0
    for x in range (len(newArr)-1):
        totalD+=findDistance(originalNodePath[newArr[x]][0],originalNodePath[newArr[x]][1],originalNodePath[newArr[x+1]][0],originalNodePath[newArr[x+1]][1])
    totalD += findDistance(originalNodePath[newArr[len(newArr)-1]][0], originalNodePath[newArr[len(newArr)-1]][1],originalNodePath[newArr[0]][0], originalNodePath[newArr[0]][1])
    return totalD

#MAIN

input = "cursor"
start = time.time()
nodes = {}
path = []

#use travelingsalesman3.py for dau file
with open("KAD.txt","r") as ins:
    for lines in ins:
        temp = lines.split()
        if len(temp) > 1:
            nodes[float(temp[0])/1000] = float(temp[1])/1000
            path.append((float(temp[0])/1000,float(temp[1])/1000))
oldPath = path.copy()


root = tkinter.Tk()
myframe = Frame(root)
h = 500
w = 800
mycanvas = Canvas(root,width=w,height=h)
mycanvas.pack()
scale = 225
varx = 9200
vary = -2400

originalNodePath = path.copy()
totalDistance = 0
for x in range(len(path)-1):
    print("Node",x,"to Node",x+1)
    totalDistance+=findDistance(path[x][1],path[x][0],path[x+1][1],path[x+1][0])
print("Node",37,"(",path[len(path)-1][0],",",path[len(path)-1][1],")","to node",0,"(",path[len(path)-1][0],",",path[len(path)-1][1],") has a distance of",findDistance(path[len(path)-1][0],path[len(path)-1][1],path[0][0],path[0][1]))
totalDistance += findDistance(path[len(path)-1][1], path[len(path)-1][0], path[0][1], path[0][0])
print("Total Distance Traveled Was",totalDistance,"kilometers")
oldTotalDistance = totalDistance


try:
    while True:
        circles = []
        for x in nodes:
            circle(mycanvas, ((float(x) * scale) - varx), (h - (float(nodes[x])) * scale - vary), 1,"red")
        circle(mycanvas, ((float(path[0][0]) * scale) - varx), (h - (float(path[0][1])) * scale - vary), 1, "blue")
        circle(mycanvas, ((float(path[len(path)-1][0]) * scale) - varx), (h - (float(path[len(path)-1][1])) * scale - vary), 1, "blue")
        for x in range(len(path)-1):
            mycanvas.create_line(((path[x][0]) * scale) - varx, (h - (path[x][1]) * scale) - vary,(float(path[x+1][0]) * scale) - varx, (h - (path[x+1][1]) * scale) - vary)
        mycanvas.create_line(((path[len(path)-1][0]) * scale) - varx, (h - (path[len(path)-1][1]) * scale) - vary,(float(path[0][0]) * scale) - varx, (h - (path[0][1]) * scale) - vary)
        Tk.update_idletasks(root)
        Tk.update(root)
        root.bind("<Key>", lambda e: root.destroy())
except:
    try:
        print("\n\n\n")
        root = tkinter.Tk()
        myframe = Frame(root)
        mycanvas = Canvas(root, width=w, height=h)
        mycanvas.pack()
        print("New Path")
        print(path)
        path = untangle(path)
        while True:
            circles = []
            for x in nodes:
                circle(mycanvas, ((float(x) * scale) - varx), (h - (float(nodes[x])) * scale - vary), 1, "red")
            circle(mycanvas, ((float(path[0][0]) * scale) - varx), (h - (float(path[0][1])) * scale - vary), 1, "blue")
            circle(mycanvas, ((float(path[len(path) - 1][0]) * scale) - varx),
                   (h - (float(path[len(path) - 1][1])) * scale - vary), 1, "blue")
            for x in range(len(path) - 1):
                mycanvas.create_line(((path[x][0]) * scale) - varx, (h - (path[x][1]) * scale) - vary,
                                     (float(path[x + 1][0]) * scale) - varx, (h - (path[x + 1][1]) * scale) - vary)
            mycanvas.create_line(((path[len(path) - 1][0]) * scale) - varx,
                                 (h - (path[len(path) - 1][1]) * scale) - vary, (float(path[0][0]) * scale) - varx,
                                 (h - (path[0][1]) * scale) - vary)
            Tk.update_idletasks(root)
            Tk.update(root)
            root.focus_force()
            root.bind("<Key>", lambda e: root.destroy())
    except:
        print("\n\n\n")
        root = tkinter.Tk()
        myframe = Frame(root)
        mycanvas = Canvas(root, width=w, height=h)
        mycanvas.pack()
        print("New Path")
        print(path)
        path = untangle(path)
        print("Print new path distance:",findPathDistance(path))
        path = permut(path)

        totalDistance = 0
        for x in range(len(path) - 1):
            totalDistance += findDistance(path[x][1], path[x][0], path[x + 1][1], path[x + 1][0])
        totalDistance += findDistance(path[len(path) - 1][1], path[len(path) - 1][0], path[0][1], path[0][0])
        print("Old Path")
        arr = []
        for x in range(38):
            arr.append(x)
        print("Old Total",arr,oldTotalDistance)
        arr = []
        for x in range(38):
            arr.append(oldPath.index(path[x]))
        while arr[0] != 0:
            arr.append(arr.pop(0))
        if arr[1] > arr[len(arr)-1]:
            arr[1:len(arr)] = arr[1:len(arr)][::-1]
        try:
            while True:
                circles = []
                for x in nodes:
                    circle(mycanvas, ((float(x) * scale) - varx), (h - (float(nodes[x])) * scale - vary), 1,"red")
                circle(mycanvas, ((float(path[0][0]) * scale) - varx), (h - (float(path[0][1])) * scale - vary), 1, "blue")
                circle(mycanvas, ((float(path[len(path)-1][0]) * scale) - varx), (h - (float(path[len(path)-1][1])) * scale - vary), 1, "blue")
                for x in range(len(path)-1):
                    mycanvas.create_line(((path[x][0]) * scale) - varx, (h - (path[x][1]) * scale) - vary,(float(path[x+1][0]) * scale) - varx, (h - (path[x+1][1]) * scale) - vary)
                mycanvas.create_line(((path[len(path)-1][0]) * scale) - varx, (h - (path[len(path)-1][1]) * scale) - vary,(float(path[0][0]) * scale) - varx, (h - (path[0][1]) * scale) - vary)
                Tk.update_idletasks(root)
                Tk.update(root)
                root.focus_force()
                root.bind("<Key>", lambda e: root.destroy())
        except:
            exit(0)
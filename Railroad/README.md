# Railroad

Railroad is a visual representation of the a\* greedy algorithm.  It seeks to find the shortest distance between any two nodes, or in this case stations.  Given two stations, it will find the shortest distance between the two stations and display the traveled path.
There are two versions of this program:  

    Railroad Romania which tracks the railroad stations in Romania
    Railroad USA which tracks the railroad stations in the USA

## Railroad USA
 
Railroad USA is a visual representation of the a\* greedy algorithm.  It seeks to find the shortest distance between any two nodes, or in this case stations in the USA.  Given two stations, it will find the shortest distance between the two stations and display the traveled path.  A map is generated, displaying all untraveled nodes in pink, possible nodes to visit in green, and traveled nodes in blue.  The final path is displayed as a red line.  Enter two different cities that contain a station to find the shortest path between them.  A list of possible stations is contained in the file cities.txt.  

  To run this program use the following commands:

    python3 railroad.py '[Station 1]' '[Station 2]'

  Note that tkinter must be installed for this program to work.
  
  This should produce a result similiar to the one below.

![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Railroad/RailroadUSA/example.gif)

## Railroad Romania

Railroad Romania is a visual representation of the a\* greedy algorithm.  It seeks to find the shortest distance between any two nodes, or in this case stations in the USA.  Given two stations, it will find the shortest distance between the two stations and display the traveled path.  A map is generated, displaying all untraveled nodes in yellow, possible nodes to visit in red, and traveled nodes in blue.  The final path is displayed as a green line.  Enter two different cities that contain a station to find the shortest path between them.  A list of possible stations is contained in the file cities.txt.  

  To run this program use the following commands:

    python3 railroad.py '[Station 1]' '[Station 2]'

  Note that tkinter must be installed for this program to work.
  
  This should produce a result similiar to the one below.
 
![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Railroad/RailroadRomania/example.png)

## 8Explore2
 
Explore2 runs 100 simulated test cases for the 8puzzle.  The average distance from goal is generated, as well as average run time.  It also takes the final case, and works backwards to determine the case that is farthest from goal.

  To run this program use the following commands:

    python3 8explore2.py
  
  This should produce a result similiar to the one below.

![Example](https://raw.githubusercontent.com/z-ng/Artificial_Intelligence/main/Slider_Puzzle/8Puzzle/explore2.png)

## 8Explore
 
Explore determines how many cases there are for how many moves must be completed.  For instance, there's only one case where 1 move must be completed before the puzzle is solved.  At 18 moves there are 9529 cases. 

  To run this program use the following commands:

    python3 8explore2.py
  
  This should produce a result similiar to the one below.

![Example](https://raw.githubusercontent.com/z-ng/Artificial_Intelligence/main/Slider_Puzzle/8Puzzle/explore.png)


## 8fast 

Fast returns the optimal moveset for a given puzzle state for the 8 puzzle.

  To run this program use the following commands:

    python3 15astar.py '[Puzzle state]'

  Please ensure that the puzzle state entered is a valid puzzle state.

  ![Example](https://raw.githubusercontent.com/z-ng/Artificial_Intelligence/main/Slider_Puzzle/8Puzzle/fast.gif)

  The input used for the example above was: "241753_86"



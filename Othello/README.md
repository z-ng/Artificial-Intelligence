# Othello

This repository contains a set of programs to play the othello board game.  Othello is a board where you seek to obtain the most tokens of your own color, while minimizing those of your opponents.  Tokens can be obtained if a straight line can be drawn directly from the placed token to another token of the same color on the board.  More information on the Othello can be found [here](https://en.wikipedia.org/wiki/Reversi).  The competition site for TJHSST can be found [here](https://othello.tjhsst.edu/play).  This particular program uses the negamax algorithm and alpha beta pruning to optimize move choices, as well as seeking out ways to reduce mobility.  If you wish to see a more organized breakdown on how this lab was put together, feel free to refer to the lab folder in this repository.  Some highlighted portions are shown below.  

## Strategy

  Strategy is the final version of the Othello bot.  It implements a variety of heuristics and algorithms such as alpha beta pruning and the negamax/minimax algorithm to optimize move choices.  This results in token capture rate of 85-90% on average.  The program takes in a board state, and returns the best possible move.  You can test the program by inputting a board state yourself or running the program against the moderator program.  

  To run this program use the following command(s):
  
    python3 strategy.py '[Board state]'

  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py strategy.py '[Number of games]'

    This will produce a similiar output to the one below:
    
  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/example.gif)	


## OthelloPlayer

  OthelloPlayer is a version of the program that takes in human input, allowing the user to play a game against the computer.  This program uses the mscvrt package and can only be run on a Windows machine as a   result.

  To run this program use the following command(s):

    python3 OthelloPlayer.py

  This will produce a similiar output to the one below:
    
  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/player.gif)	

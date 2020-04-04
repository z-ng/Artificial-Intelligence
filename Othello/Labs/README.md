# Othello

This repository contains a set of programs to play the othello board game.  Othello is a board where you seek to obtain the most tokens of your own color, while minimizing those of your opponents.  Tokens can be obtained if a straight line can be drawn directly from the placed token to another token of the same color on the board.  More information on the Othello can be found [here](https://en.wikipedia.org/wiki/Reversi).  The competition site for TJHSST can be found [here](https://othello.tjhsst.edu/play).  This particular program uses the negamax algorithm and alpha beta pruning to optimize move choices.  There are various versions of this program.  Generally, each version of the program gets progressively more complex, and is tailored to each assignment's specifications.  This includes all files used for this project, if you wish to see a more brief and summarized version please refer to the root of this repository.

## Othello1 

  Othello1 is the baseline program.  It is able to determine the possible moves given an othello board state, and can determine the current player's turn.

  To run this program use the following command(s):

    python3 Othello1.py '[Board state]'

  For example, the board state for "...XOXO.OXOXO.XOO...XOO........O.XXOXOO...XO.............XOXOO.." would be:

  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/Othello1.png)


  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py Othello1.py

## Othello2 

  Othello1 takes in an input board and calculates the current score of the state of the board.

  To run this program use the following command(s):

    python3 Othello2.py '[Board state]'

  For example, the output for "...XOXO.OXOXO.XOO...XOO........O.XXOXOO...XO.............XOXOO.." would be:

  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/Othello2.png)

## Othello3 

  Othello1 takes in an input board and a move and provides an updated board state and scoreboard to match the movie.

  To run this program use the following command(s):

    python3 Othello3.py '[Board state]' '[Position #]'

  For example, the output for "...XOXO.OXOXO.XOO...XOO........O.XXOXOO...XO.............XOXOO.. 13" would be:

  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/Othello3.png)

## Othello4

  Othello4 is a version of the program that takes in human input, allowing the user to play a game against the computer.  This program uses the mscvrt package and can only be run on a Windows machine as a   result.

  To run this program use the following command(s):

    python3 Othello4.py

  This will produce a similiar output to the one below:
    
  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/player.gif)	

## Othello5
  
  Othello 5 is a program that returns possible moves given a board state.

  To run this program use the following command(s):
  
    python3 Othello5.py '[Board state]'

  For example, the output for "...XOXO.OXOXO.XOO...XOO........O.XXOXOO...XO.............XOXOO.." would be:

  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/Othello5.png)	

  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py Othello5.py

## Othello6

  Othello 6 is an improved version of previous Othello programs that applies some heuristics to improve the win percentage.

  To run this program use the following command(s):
  
    python3 Othello6.py '[Board state]'

  For example, the output for "...XOXO.OXOXO.XOO...XOO........O.XXOXOO...XO.............XOXOO.." would be:

  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/Othello6.png)	

  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py Othello6.py

## Othello7

  Othello 7 further improves on heuristics, and applies the negamax algorithm to further optimize win precentage.  Depending on the depth of the search, negamax will return a particular moveset.  It will the weight each of the moves respectively, and return the optimal moveset.

  To run this program use the following command(s):
  
    python3 Othello7.py '[Board state]'

  For example, the output for "...XOXO.OXOXO.XOO...XOO........O.XXOXOO...XO.............XOXOO.." would be:

  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/Othello7.png)	

  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py Othello7.py

## OthelloAC

  Othello A-C further improves on the program.  These implemented alpha beta and negamax, as well as additional heuristics.

  To run this program use the following command(s):
  
    python3 OthelloA.py '[Board state]'

  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py OthelloA.py

## Strategy

  Strategy is the version of the Othello bot.  In addition to including previous improvements, it emphasizes moves that result in a reduction of enemy mobility.

  To run this program use the following command(s):
  
    python3 strategy.py '[Board state]'

  You can also run test this program against the moderator program using the following:
    
    python3 moderator.py strategy.py

## Test

  The program sets denoted by "test" attempt to maximize the amount of tokens gained by the player rather than simply trying to win.  Test3 is the most complex followed by test 2 and test 1.  They implement alpha beta pruning along with negamax to reduce the amount of tokens gained by the opponent.

  To run this program use the following commands(s)

    python3 moderator.py test.py test3.py '[Number of rounds]'

  This would produce a similiar output to hte one below:
    
  ![Example](https://raw.githubusercontent.com/zac-ng/Artificial_Intelligence/main/Othello/Labs/test.gif)	




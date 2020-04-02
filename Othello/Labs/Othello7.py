import time
import sys

def totalTokens(game):
    count = 0
    for x in game:
        if x == ".":
            count+=1
    return count
def display(game):
    for x in range(8):
        print(" ".join(game[0+(8*x):8+(8*x)]))
def findTurn(game):
    if (game.count("X")+game.count("x")) %2 == 0:
        return "X"
    return "O"
def findVerticalPossible(game,nextMove,index):
    s = set()
    pos = index-8
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove:
        if game[pos] == ".":
            space = pos
        pos = pos-8
    if space != index-8 and space != -1:
        s.add(space)
    pos = index+8
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove:
        if game[pos] == ".":
            space = pos
        pos = pos+8
    if space != index+8 and space != -1:
        s.add(space)
    return s
def findHorizontalPossible(game,nextMove,index):
    s = set()
    pos = index-1
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and pos//8 == index//8:
        if game[pos] == ".":
            space = pos
        pos = pos-1
    if space != index-1 and space != -1 and space//8 == index//8:
        s.add(space)
    pos = index+1
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and pos//8 == index//8:
        if game[pos] == ".":
            space = pos
        pos = pos+1
    if space != index+1 and space != -1 and space//8 == index//8:
        s.add(space)
    return s
def findDiagnolsPossible(game,nextMove,index):
    s = set()
    pos = index-7
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and (pos+7)//8 != pos//8:
        if game[pos] == ".":
            space = pos
        pos = pos-7
    if space != index-7 and space != -1:
        #print(space,"1")
        s.add(space)
    pos = index+7
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-7)//8 != pos//8:
        if game[pos] == ".":
            space = pos
        pos = pos+7
    if space != index+7 and space != -1:
        #print(space,"2")
        s.add(space)

    pos = index-9 #other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and (pos+9)//8 != pos//8 and ((pos+9)//8)-(pos//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos-9
    if space != index-9 and space != -1:
        #print(index,space,"3")
        s.add(space)
    pos = index+9
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-9)//8 != pos//8 and (pos//8)-((pos-9)//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos+9
    if space != index+9 and space != -1:
        #print(index,space,"4")
        s.add(space)
    return s
def findVertical(game,nextMove,index):
    board = game
    pos = index-8
    space = -1
    while space < 0 and pos >= 0 and game[pos] != ".":
        if game[pos] == nextMove:
            space = pos
        pos = pos-8
    if space != index-8 and space != -1:
        while pos != index-8:
            pos = pos+8
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+8
    space = -1
    while space < 0 and pos < 64 and game[pos] != ".":
        if game[pos] == nextMove:
            space = pos
        pos = pos+8
    if space != index+8 and space != -1:
        while pos != index+8 and pos > 0:
            pos = pos-8
            board = board[:pos] + nextMove + board[pos+1:]
    return board
def findHorizontal(game,nextMove,index):
    board = game
    pos = index-1
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and pos//8 == index//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos-1
    if space != index-1 and space != -1 and space//8 == index//8:
        while pos != index:
            pos = pos+1
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+1
    space = -1
    while space < 0 and pos < 64 and game[pos] != "."  and pos//8 == index//8: # maybe add pos%8 != 0
        if game[pos] == nextMove:
            space = pos
        pos = pos+1
    if space != index+1 and space != -1 and space//8 == index//8:
        while pos != index and pos > 0:
            pos = pos-1
            board = board[:pos] + nextMove + board[pos+1:]
    return board
def findDiagnols(game,nextMove,index):
    board = game
    pos = index-7
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos+7)//8 != pos//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos-7
    if space != index-7 and space != -1:
        while pos != index-7 and pos > 0:
            pos = pos+7
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+7
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos-7)//8 != pos//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos+7
    if space != index+7 and space != -1: #try to add this to all and pos//8 != space//8 may not be neccessary
        while pos != index+7 and pos > 0:
            pos = pos-7
            board = board[:pos] + nextMove + board[pos+1:]

    pos = index-9 #other diagnol
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos+9)//8 != pos//8 and ((pos+9)//8)-(pos//8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos-9
    if space != index and space != -1 and pos//8 != space//8:
        while pos != index-9 and pos > 0:
            pos = pos+9
            board = board[:pos] + nextMove + board[pos+1:]
    pos = index+9
    space = -1
    while space < 0 and pos < 64 and game[pos] != "." and (pos-9)//8 != pos//8 and (pos//8)-((pos-9)//8) <= 1:
        if game[pos] == nextMove:
            space = pos
        pos = pos+9
    if space != index+9 and space != -1 and pos//8 != space//8:
        while pos != index+9 and pos > 0:
            pos = pos-9
            board = board[:pos] + nextMove + board[pos+1:]
    return board
def flipBoard(game,token,position):
    board = findVertical(game,token,position)
    board = findHorizontal(board,token,position)
    board = findDiagnols(board,token,position)
    return board
def findPossibleMoves(game,nextMove):
    moves = set()
    for x in range(64):
        if game[x] == nextMove:
            moves = moves|findVerticalPossible(game,nextMove,x)
            moves = moves|findHorizontalPossible(game,nextMove,x)
            moves = moves|findDiagnolsPossible(game,nextMove,x)
    return moves
def evalBoard(board,token):
    xCount = board.count("X")
    oCount = board.count("O")
    if token == "X":
        return xCount-oCount
    return oCount-xCount
def makeMove(board,token,mv):
    return flipBoard(board,token,mv)
def negamax(board, token, levels):
    if not levels:
      return [evalBoard(board, token)]
    lm = findPossibleMoves(board+'',token)
    best = []
    if not lm:
      enemy = findTurn(board)
      best = negamax(board, enemy, levels - 1) + [-1]
    else:
      for mv in lm:
          enemy = findTurn(board)
          best = best+[negamax(makeMove(board, token, mv), enemy, levels-1) + [mv]]
      best = sorted(best)[0]
    if len(best) != 0:
      return [-best[0]] + best[1:]
    else:
      return []

game = "...........................OX......XO..........................."
nextMove = "H"
if len(sys.argv) > 1:
    if len(''.join(sys.argv[1])) > 2:
        game = ''.join(sys.argv[1])
    else:
        nextMove = ''.join(sys.argv[1]).upper()
if len(sys.argv) > 2:
    if len(''.join(sys.argv[2])) > 2:
        game = ''.join(sys.argv[2])
    else:
        nextMove = ''.join(sys.argv[2]).upper()
if nextMove == "H":
    if totalTokens(game)%2 == 0:
        nextMove = "X"
    else:
        nextMove = "O"
for x in range(64):
    if game[x] == "x" or game[x] == "o":
        game = game[:x]+ game[x].upper()+game[x+1:]
display(game)
print(game)
moves = findPossibleMoves(game,nextMove)
nm = negamax(game, nextMove, 5)
print("At level {}, nm gives {}".format(5, nm))
print("and I pick {}".format(nm[-1]))
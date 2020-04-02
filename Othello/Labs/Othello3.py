import time
import sys

def display(game):
    for x in range(8):
        print(" ".join(game[0+(8*x):8+(8*x)]))
def displayScore(board):
    xCount = 0
    oCount = 0
    for x in board:
        if x == "X":
            xCount = xCount+1
        elif x == "O":
            oCount = oCount+1
    print("X Score:",xCount,"O Score:",oCount)

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
    while space < 0 and pos < 64 and game[pos] != "."  and pos//8 == index//8:
        if game[pos] == nextMove:
            space = pos
        pos = pos+1
    if space != index+1 and space != -1 and space//8 == index//8:
        while pos != index and pos > 0:
            pos = pos-1
            board = board[:pos] + nextMove + board[pos+1:]
    return board

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

def findDiagnols(game,nextMove,index):
    board = game
    pos = index-7
    space = -1
    while space < 0 and pos >= 0 and game[pos] != "." and (pos+7)//8 != pos//8:
        if game[pos] == nextMove:
            space = pos
            break;
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
    if space != index+7 and space != -1:
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
    while space < 0 and pos < 64 and game[pos] != nextMove and pos//8 and index//8:
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

    pos = index-9
    space = -1
    while space < 0 and pos >= 0 and game[pos] != nextMove and (pos+9)//8 != pos//8 and ((pos+9)//8)-(pos//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos-9
    if space != index-9 and space != -1:
        s.add(space)
    pos = index+9
    space = -1
    while space < 0 and pos < 64 and game[pos] != nextMove and (pos-9)//8 != pos//8 and (pos//8)-((pos-9)//8) <= 1:
        if game[pos] == ".":
            space = pos
        pos = pos+9
    if space != index+9 and space != -1:
        s.add(space)
    return s
def findPossibleMoves(game,nextMove):
    moves = set()
    for x in range(64):
        if game[x] == nextMove:
            moves = moves|findVerticalPossible(game,nextMove,x)
            moves = moves|findHorizontalPossible(game,nextMove,x)
            moves = moves|findDiagnolsPossible(game,nextMove,x)
    return moves

def flipBoard(game,token,position):
    board = findVertical(game,token,position)
    board = findHorizontal(board,token,position)
    board = findDiagnols(board,token,position)
    return board
def totalTokens(game):
    count = 0
    for x in game:
        if x != ".":
            count+=1
    return count
def findNextMove(game):
    if (64-game.count("."))%2 == 0:
        return "X"
    return "O"

board = "...........................OX......XO..........................."
posLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
token = "X"
position = []
if len(sys.argv) > 1:
    if len(''.join(sys.argv[1])) == 64:
        board = ''.join(sys.argv[1])
        token = findNextMove(board)
    elif ''.join(sys.argv[1]).upper() == "X" or ''.join(sys.argv[1]).upper() == "O":
        token = ''.join(sys.argv[1]).upper()
    else:
        position = (sys.argv[1:len(sys.argv)])
if len(sys.argv) > 2:
    if len(''.join(sys.argv[2])) == 64:
        board = ''.join(sys.argv[2])
        token = findNextMove(board)
    elif ''.join(sys.argv[2]).upper() == "O" or ''.join(sys.argv[2]).upper() == "X":
        token = ''.join(sys.argv[2]).upper()
    elif len(position) == 0:
        position = sys.argv[2:len(sys.argv)]
if len(sys.argv) > 3:
    if len(''.join(sys.argv[3])) == 64:
        board = ''.join(sys.argv[3])
        token = findNextMove(board)
    elif ''.join(sys.argv[3]).upper() == "X" or ''.join(sys.argv[1]).upper() == "O":
        token = ''.join(sys.argv[3]).upper()
    elif len(position) == 0:
        position = sys.argv[3:len(sys.argv)]
token = findNextMove(board)
board = board.upper()
token = token.upper()
if len(position) == 0:
    display(board)
    print(board,end = " ")
    displayScore(board)
    exit(0)
print(board)
display(board)
print(board,end = " ")
displayScore(board)
#print(position)
for x in position:
    print(x)
    if x[0].lower() in posLetters:
        index = (ord(x[0].lower()) - 97) + ((int(x[1]) - 1) * 8)
    else:
        index = x
    if int(index) not in findPossibleMoves(board,token):
        print("Token",token,findPossibleMoves(board,token))
        if token == "X" or token == "x":
            token = "O"
        else:
            token = "X"
    board = board[:int(index)]+token+board[int(index)+1:]
    board = flipBoard(board,token,int(index))
    print("")
    display(board)
    print(board, end = " ")
    displayScore(board)
    token = findNextMove(board)